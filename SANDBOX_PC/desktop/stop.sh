#!/bin/sh
# End the desktop session: the X server goes, and every window with it.
me=$(id -u)
pkill -u "$me" -x tint2; pkill -u "$me" -x openbox; pkill -u "$me" -x Xvfb
sleep 0.3
pkill -u "$me" -f 'dbus-daemon --session --address=unix:path=/tmp/argus-desk/run/bus'
rm -rf /tmp/argus-desk/run /tmp/.X1-lock /tmp/.X11-unix/X1
echo STOPPED
