"""The sandbox computer's screen, as pictures on stdout (run in the sandbox: python3 /opt/desktop/screen.py).

    screen.py --once                 one JPEG of display :1, then exit
    screen.py [--fps 12] [--quality 70]
                                     an endless multipart stream (boundary "argusframe"): a new picture whenever the
                                     screen changed, and one a second when it did not; ends when nobody reads it

Nothing is listened on: the pictures leave through the `docker exec` that started this (no port, as for everything
in the sandbox). The X pointer is not in the pictures; the page shows its own over them.
"""

import argparse
import io
import sys
import time
import zlib

from PIL import Image
from Xlib import X, display

BOUNDARY = b"argusframe"


def grab(root, width: int, height: int) -> bytes:
    return root.get_image(0, 0, width, height, X.ZPixmap, 0xFFFFFFFF).data


def jpeg(raw: bytes, width: int, height: int, quality: int) -> bytes:
    picture = Image.frombytes("RGB", (width, height), raw, "raw", "BGRX")
    out = io.BytesIO()
    picture.save(out, "JPEG", quality=quality)
    return out.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--fps", type=float, default=12.0)
    parser.add_argument("--quality", type=int, default=70)
    args = parser.parse_args()
    try:
        screen = display.Display()
    except Exception as error:  # no X server on DISPLAY: the desktop is off
        print(f"no display: {error}", file=sys.stderr)
        return 3
    root = screen.screen().root
    size = root.get_geometry()
    width, height = size.width, size.height
    out = sys.stdout.buffer
    if args.once:
        out.write(jpeg(grab(root, width, height), width, height, args.quality))
        out.flush()
        return 0
    step = 1.0 / max(1.0, min(30.0, args.fps))
    last, sent = None, 0.0
    try:
        while True:
            began = time.monotonic()
            raw = grab(root, width, height)
            mark = zlib.adler32(raw)
            if mark != last or began - sent >= 1.0:  # (the one a second keeps the stream, and its end, noticed)
                data = jpeg(raw, width, height, args.quality)
                out.write(b"--" + BOUNDARY + b"\r\nContent-Type: image/jpeg\r\nContent-Length: " + str(len(data)).encode()
                          + b"\r\nX-Screen: " + f"{width}x{height}".encode() + b"\r\n\r\n" + data + b"\r\n")
                out.flush()
                last, sent = mark, began
            time.sleep(max(0.0, step - (time.monotonic() - began)))
    except (BrokenPipeError, ConnectionResetError, KeyboardInterrupt):
        return 0  # nobody reads any more
    except Exception as error:  # the X server went (the desktop was stopped)
        print(f"screen ended: {error}", file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
