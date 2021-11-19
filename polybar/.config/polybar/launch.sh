#!/usr/bin/env sh

## Add this to your wm startup file.

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# pkill -F /tmp/polybar-music.pid
# rm /tmp/polybar-music.pid

# Launch bar1 and bar2
# polybar left 2>~/.config/polybar/logs/left.log &
# polybar middle 2>~/.config/polybar/logs/middle.log &
# polybar right 2>~/.config/polybar/logs/right.log &
# ~/.config/polybar/music_bar.py 2>~/.config/polybar/logs/music.log &
polybar -c ~/.config/polybar/config.ini full 2>~/.config/polybar/logs/full.log
