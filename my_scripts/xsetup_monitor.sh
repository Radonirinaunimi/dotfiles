#!/bin/sh
xrandr --output DP2 --auto
echo "Trun on Dell monitor"
xrandr --output eDP1 --mode 1920x1080 --below DP2
