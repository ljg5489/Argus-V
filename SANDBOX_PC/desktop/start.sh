#!/bin/sh
# Start the desktop session on display :1, or leave the one that runs. Says READY <width>x<height> or FAILED <why>.
# Everything it writes goes to /tmp/argus-desk (not /workspace: a socket or a link there would stop sandbox.py's
# snapshots, and with them every later command). HOME stays /workspace/.home, as for every command in the sandbox.
W=${1:-1024}; H=${2:-640}
D=/tmp/argus-desk
mkdir -p "$D/run" "$D/config" "$D/cache" && chmod 700 "$D/run"
export DISPLAY=:1 LANG=C.UTF-8 TZ=KST-9 SHELL=/bin/bash XDG_RUNTIME_DIR="$D/run" XDG_CONFIG_HOME="$D/config" XDG_CACHE_HOME="$D/cache"
export LIBGL_ALWAYS_SOFTWARE=1 GALLIUM_DRIVER=llvmpipe LP_NUM_THREADS=2 NO_AT_BRIDGE=1 SDL_AUDIODRIVER=dummy
cd /workspace 2>/dev/null || cd /
if ! xdpyinfo >/dev/null 2>&1; then
  rm -f /tmp/.X1-lock /tmp/.X11-unix/X1
  setsid Xvfb :1 -screen 0 "${W}x${H}x24" -nolisten tcp -ac -noreset +extension GLX +extension XTEST >"$D/run/xvfb.log" 2>&1 &
  n=0
  until xdpyinfo >/dev/null 2>&1; do
    n=$((n + 1))
    if [ "$n" -gt 60 ]; then echo "FAILED Xvfb: $(tail -c 300 "$D/run/xvfb.log" | tr '\n' ' ')"; exit 1; fi
    sleep 0.1
  done
  setxkbmap us >/dev/null 2>&1
  xsetroot -solid '#3f2c25' >/dev/null 2>&1
  fresh=1
fi
if [ ! -S "$D/run/bus" ]; then
  dbus-daemon --session --address="unix:path=$D/run/bus" --fork --nopidfile >/dev/null 2>&1
fi
export DBUS_SESSION_BUS_ADDRESS="unix:path=$D/run/bus"
me=$(id -u)
pgrep -u "$me" -x openbox >/dev/null || setsid openbox >"$D/run/openbox.log" 2>&1 &
pgrep -u "$me" -x tint2 >/dev/null || setsid tint2 -c /opt/desktop/tint2rc >"$D/run/tint2.log" 2>&1 &
if [ -n "$fresh" ]; then  # the first look: one terminal, in the work folder
  (sleep 0.6; setsid lxterminal --working-directory=/workspace >"$D/run/terminal.log" 2>&1 &) &
fi
echo "READY $(xdpyinfo 2>/dev/null | awk '/dimensions:/{print $2; exit}')"
