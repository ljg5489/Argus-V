"""What gui-run and sandbox-info share: the sandbox's screen (display :1), whether it is on, and its windows."""

import subprocess
import time

DISPLAY = ":1"
START = "/opt/desktop/start.sh"
NOT_PROGRAMS = {"_NET_WM_WINDOW_TYPE_DOCK", "_NET_WM_WINDOW_TYPE_DESKTOP"}  # the bar and the background


def size() -> str | None:
    """"1024x640" when the screen is on, else None."""
    try:
        done = subprocess.run(["xdpyinfo", "-display", DISPLAY], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if done.returncode != 0:
        return None
    for line in done.stdout.splitlines():
        if "dimensions:" in line:
            return line.split()[1]
    return "on"


def turn_on() -> str | None:
    """Start the desktop when it is off. -> a line saying so (None: it was on); RuntimeError when it does not start."""
    if size():
        return None
    try:
        done = subprocess.run([START], capture_output=True, text=True, timeout=45)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise RuntimeError(f"the screen could not be turned on: {type(error).__name__}") from error
    if "READY" not in done.stdout:
        raise RuntimeError("the screen could not be turned on: " + (done.stdout + done.stderr).strip()[-300:])
    time.sleep(1.2)  # (the window manager and its first window settle)
    return "The screen was off: it is on now (" + done.stdout.split("READY", 1)[1].strip() + ")."


def windows() -> list[dict]:
    """The program windows on the screen: [{"id", "title", "width", "height", "pid"}] ([] when the screen is off)."""
    try:
        from Xlib import X, display
    except Exception:
        return []
    try:
        screen = display.Display(DISPLAY)
    except Exception:
        return []
    found = []
    try:
        atom = screen.intern_atom
        listed = screen.screen().root.get_full_property(atom("_NET_CLIENT_LIST"), X.AnyPropertyType)
        for number in (listed.value if listed else []):
            try:
                window = screen.create_resource_object("window", int(number))
                kind = window.get_full_property(atom("_NET_WM_WINDOW_TYPE"), X.AnyPropertyType)
                if {screen.get_atom_name(int(value)) for value in (kind.value if kind else [])} & NOT_PROGRAMS:
                    continue
                name = window.get_full_property(atom("_NET_WM_NAME"), atom("UTF8_STRING"))
                title = name.value.decode("utf-8", "replace") if name is not None and isinstance(name.value, bytes) else (window.get_wm_name() or "")
                shape = window.get_geometry()
                owner = window.get_full_property(atom("_NET_WM_PID"), X.AnyPropertyType)
                found.append({"id": int(number), "title": str(title), "width": int(shape.width), "height": int(shape.height),
                              "pid": int(owner.value[0]) if owner is not None and len(owner.value) else None})
            except Exception:  # a window that closed while it was being read
                continue
    except Exception:
        pass
    finally:
        try:
            screen.close()
        except Exception:
            pass
    return found


# ---------------------------------------------------------------------------- the screen in words (gui-look, gui-run)
# A model that reads text cannot look at what it drew. These say what a picture is in words and numbers: whether it is
# one flat color (nothing drawn), which colors fill it, where they lie, and whether anything moves.
PALETTE = (("K", "black", (0, 0, 0)), ("D", "dark gray", (64, 64, 64)), ("A", "gray", (128, 128, 128)),
           ("L", "light gray", (200, 200, 200)), ("W", "white", (255, 255, 255)), ("R", "red", (220, 30, 30)),
           ("r", "dark red", (120, 20, 20)), ("O", "orange", (240, 140, 30)), ("Y", "yellow", (240, 220, 40)),
           ("G", "green", (40, 170, 60)), ("g", "dark green", (20, 90, 40)), ("C", "cyan", (60, 200, 210)),
           ("B", "blue", (50, 90, 220)), ("b", "dark blue", (20, 30, 110)), ("S", "sky blue", (120, 170, 235)),
           ("P", "purple", (140, 60, 180)), ("p", "pink", (240, 150, 190)), ("N", "brown", (130, 85, 45)))
FLAT = 0.97          # a picture of which this much is one color has nothing drawn in it
GRID = (16, 8)       # columns and rows of the map of a picture
SMALL = (160, 100)   # a picture is looked at this small


def nearest(color) -> tuple[str, str]:
    """(letter, name) of the palette color nearest to an (r, g, b)."""
    red, green, blue = color[:3]
    letter, name, _rgb = min(PALETTE, key=lambda item: (item[2][0] - red) ** 2 + (item[2][1] - green) ** 2 + (item[2][2] - blue) ** 2)
    return letter, name


def grab():
    """The whole screen as a picture (None when it is off or cannot be read)."""
    try:
        from PIL import Image
        from Xlib import X, display
        screen = display.Display(DISPLAY)
    except Exception:
        return None
    try:
        root = screen.screen().root
        shape = root.get_geometry()
        raw = root.get_image(0, 0, shape.width, shape.height, X.ZPixmap, 0xFFFFFFFF).data
        return Image.frombytes("RGB", (shape.width, shape.height), raw, "raw", "BGRX")
    except Exception:
        return None
    finally:
        try:
            screen.close()
        except Exception:
            pass


def place(number: int) -> tuple[int, int, int, int] | None:
    """Where a window's inside lies on the screen: (left, top, right, bottom)."""
    try:
        from Xlib import display
        screen = display.Display(DISPLAY)
    except Exception:
        return None
    try:
        root = screen.screen().root
        window = screen.create_resource_object("window", int(number))
        shape, at = window.get_geometry(), root.translate_coords(window, 0, 0)
        whole = root.get_geometry()
        box = (max(0, at.x), max(0, at.y), min(whole.width, at.x + shape.width), min(whole.height, at.y + shape.height))
        return box if box[2] - box[0] > 4 and box[3] - box[1] > 4 else None
    except Exception:
        return None
    finally:
        try:
            screen.close()
        except Exception:
            pass


def points(picture) -> list[tuple[int, int, int]]:
    """Every point of an RGB picture as (red, green, blue)."""
    data = picture.convert("RGB").tobytes()
    return [(data[index], data[index + 1], data[index + 2]) for index in range(0, len(data), 3)]


def read_picture(picture) -> dict:
    """What a picture is: {"size", "flat": (name, rgb, share) or None, "colors": [(name, share)], "map": [rows of
    letters], "legend": {letter: name}}."""
    # (every so-many-th point as it is: a blend of two colors at an edge would count as a third)
    small = picture.convert("RGB").resize((min(SMALL[0], picture.width), min(SMALL[1], picture.height)), 0)
    pixels = points(small)
    total = len(pixels) or 1
    exact = {}
    for red, green, blue in pixels:  # (the lowest bits are noise: 32 steps a channel)
        key = (red >> 3, green >> 3, blue >> 3)
        exact[key] = exact.get(key, 0) + 1
    top, count = max(exact.items(), key=lambda item: item[1])
    rgb = tuple(value * 8 + 4 for value in top)
    named = {}
    for pixel in pixels:
        name = nearest(pixel)[1]
        named[name] = named.get(name, 0) + 1
    colors = sorted(((name, amount / total) for name, amount in named.items()), key=lambda item: -item[1])
    columns, rows = GRID
    cells = small.resize((columns, rows), 4)  # (each cell: the mean of what lies in it)
    letters = [nearest(pixel) for pixel in points(cells)]
    lines = ["".join(letter for letter, _name in letters[row * columns:(row + 1) * columns]) for row in range(rows)]
    return {"size": picture.size, "flat": (nearest(rgb)[1], rgb, count / total) if count / total >= FLAT else None,
            "colors": [(name, share) for name, share in colors if share >= 0.003][:8], "map": lines,
            "legend": {letter: name for letter, name in dict.fromkeys(letters)}}


def moved(first, second) -> float:
    """The share of a picture that changed from ``first`` to ``second`` (0.0 to 1.0)."""
    width, height = min(SMALL[0], first.width, second.width), min(SMALL[1], first.height, second.height)
    one, two = first.convert("L").resize((width, height), 0).tobytes(), second.convert("L").resize((width, height), 0).tobytes()
    return sum(1 for a, b in zip(one, two) if abs(a - b) > 16) / (len(one) or 1)


def describe(read: dict, change: float | None = None, seconds: float = 1.0, grid: bool = True) -> list[str]:
    """The lines that say what read_picture() found."""
    lines = []
    if read["flat"]:
        name, rgb, share = read["flat"]
        lines.append(f"It is almost one flat color: {name} {rgb} covers {share:.0%}. Nothing is drawn in it (an empty scene, "
                     "a camera that looks at nothing, a model that did not load, or a program that only cleared the window).")
    else:
        lines.append("Colors: " + ", ".join(f"{name} {share:.0%}" if share >= 0.01 else f"{name} under 1%" for name, share in read["colors"]) + ".")
        if grid:
            lines.append(f"Where they lie, {GRID[0]} columns by {GRID[1]} rows ("
                         + ", ".join(f"{letter} {name}" for letter, name in read["legend"].items()) + "):")
            lines += ["  " + row for row in read["map"]]
    if change is not None:
        lines.append(f"Moving: {change:.1%} of it changed in {seconds:.1f} s." if change >= 0.002
                     else f"Not moving: nothing changed in {seconds:.1f} s.")
    return lines


def look(window: dict | None = None, wait: float = 1.0, grid: bool = True) -> list[str]:
    """What is on the screen (or in one window) now, as lines of text; [] when the screen cannot be read."""
    first = grab()
    if first is None:
        return []
    box = place(window["id"]) if window else None
    second = None
    if wait > 0:
        time.sleep(wait)
        second = grab()
    crop = (lambda picture: picture.crop(box)) if box else (lambda picture: picture)
    change = moved(crop(first), crop(second)) if second is not None else None
    return describe(read_picture(crop(second if second is not None else first)), change, wait, grid)
