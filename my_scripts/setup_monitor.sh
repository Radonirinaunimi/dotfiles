#!/bin/sh
xrandr --output DP1 --auto
echo "Trun on Dell monitor"
xrandr --output eDP1 --mode 1920x1080 --below DP2
echo "Switch off main screen"
xrandr --output eDP1 --off
