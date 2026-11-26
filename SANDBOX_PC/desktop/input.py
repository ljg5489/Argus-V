"""The keyboard and the mouse of the sandbox computer's screen (run in the sandbox: python3 /opt/desktop/input.py).

One JSON object a line on stdin, until stdin ends:
    {"t": "k", "key": "KeyA", "down": true}        a key by the browser's physical name (KeyboardEvent.code)
    {"t": "m", "x": 512, "y": 300}                 the pointer, in screen pixels
    {"t": "b", "button": 1, "down": true}          a mouse button (1 left, 2 middle, 3 right)
    {"t": "w", "dy": -1}                           the wheel (-1 up, 1 down), one notch a line

Keys go by physical name, so Shift is its own key and a held key stays held (a game's steering). The layout in the
sandbox is US (desktop/start.sh sets it): Korean text cannot be typed through this. What is still held when stdin ends
is let go, so no key stays stuck.
"""

import json
import sys

from Xlib import X, XK, display
from Xlib.ext import xtest

# KeyboardEvent.code -> X keysym name (the key's unshifted sign on a US keyboard)
KEYS = {
    **{f"Key{letter}": letter.lower() for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"},
    **{f"Digit{digit}": digit for digit in "0123456789"},
    **{f"F{number}": f"F{number}" for number in range(1, 13)},
    **{f"Numpad{digit}": f"KP_{digit}" for digit in "0123456789"},
    "Space": "space", "Enter": "Return", "NumpadEnter": "KP_Enter", "Tab": "Tab", "Backspace": "BackSpace",
    "Escape": "Escape", "Delete": "Delete", "Insert": "Insert", "Home": "Home", "End": "End", "PageUp": "Prior",
    "PageDown": "Next", "ArrowUp": "Up", "ArrowDown": "Down", "ArrowLeft": "Left", "ArrowRight": "Right",
    "ShiftLeft": "Shift_L", "ShiftRight": "Shift_R", "ControlLeft": "Control_L", "ControlRight": "Control_R",
    "AltLeft": "Alt_L", "AltRight": "Alt_R", "MetaLeft": "Super_L", "MetaRight": "Super_R", "CapsLock": "Caps_Lock",
    "Minus": "minus", "Equal": "equal", "BracketLeft": "bracketleft", "BracketRight": "bracketright",
    "Backslash": "backslash", "Semicolon": "semicolon", "Quote": "apostrophe", "Backquote": "grave",
    "Comma": "comma", "Period": "period", "Slash": "slash",
    "NumpadAdd": "KP_Add", "NumpadSubtract": "KP_Subtract", "NumpadMultiply": "KP_Multiply",
    "NumpadDivide": "KP_Divide", "NumpadDecimal": "KP_Decimal",
}


def main() -> int:
    try:
        screen = display.Display()
    except Exception as error:
        print(f"no display: {error}", file=sys.stderr)
        return 3
    size = screen.screen().root.get_geometry()
    codes = {name: screen.keysym_to_keycode(XK.string_to_keysym(sign)) for name, sign in KEYS.items()}
    held_keys, held_buttons = set(), set()
    try:
        for line in sys.stdin:
            try:
                event = json.loads(line)
                kind = event.get("t")
                if kind == "m":
                    x = max(0, min(size.width - 1, int(event["x"])))
                    y = max(0, min(size.height - 1, int(event["y"])))
                    xtest.fake_input(screen, X.MotionNotify, x=x, y=y)
                elif kind == "b":
                    button = int(event["button"])
                    if button in (1, 2, 3):
                        down = bool(event.get("down"))
                        xtest.fake_input(screen, X.ButtonPress if down else X.ButtonRelease, button)
                        (held_buttons.add if down else held_buttons.discard)(button)
                elif kind == "w":
                    button = 4 if int(event.get("dy", 0)) < 0 else 5
                    xtest.fake_input(screen, X.ButtonPress, button)
                    xtest.fake_input(screen, X.ButtonRelease, button)
                elif kind == "k":
                    code = codes.get(str(event.get("key")))
                    if code:
                        down = bool(event.get("down"))
                        xtest.fake_input(screen, X.KeyPress if down else X.KeyRelease, code)
                        (held_keys.add if down else held_keys.discard)(code)
                screen.flush()
            except (ValueError, KeyError, TypeError):
                continue  # a line that is not an event: passed over
    finally:
        try:
            for code in held_keys:
                xtest.fake_input(screen, X.KeyRelease, code)
            for button in held_buttons:
                xtest.fake_input(screen, X.ButtonRelease, button)
            screen.sync()
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
