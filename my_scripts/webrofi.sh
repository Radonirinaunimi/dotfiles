#!/usr/bin/env bash

surfraw -browser=firefox $(sr -elvi | awk -F'-' '{print $1}' | sed '/:/d' | awk '{$1=$1};1' | rofi -kb-row-select "Tab" -kb-row-tab "Control+space" -dmenu -i -p "Websearch")
