#!/usr/bin/env bash

surfraw -browser=firefox "$(cat ~/.config/surfraw/bookmarks | sed '/^$/d' | sed '/^#/d' | sed '/^\//d' | sort -n | rofi -dmenu -i -p "Bookmarks")"
