# -*- coding: utf-8 -*-
import os
import re
import psutil
import socket
import subprocess
from libqtile import bar
from libqtile import hook
from libqtile import widget
from libqtile import layout
from libqtile.config import Key
from libqtile.config import Drag
from libqtile.config import Click
from libqtile.command import lazy
from libqtile.config import Group
from libqtile.config import Screen
from libqtile.config import KeyChord
from libqtile.lazy import lazy
from typing import List

mod         = "mod4"                                # Sets mod key to SUPER/WINDOWS
myTerm      = "alacritty"                           # Terminal of choice
myConfig    = "/home/dt/.config/qtile/config.py"    # Qtile config file location

keys = [
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "space",
             lazy.spawn("rofi -show drun"),
             desc='Rofi Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key(["control", "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "m",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod, "shift"], "Return",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         # ROFI scripts launched with ALT + CTRL + KEY
         Key(["mod1", "control"], "b",
             lazy.spawn("./my_scripts/bookrofi.sh"),
             desc='Rofi scripts for launching bookmarks on firefox'
             ),
         Key(["mod1", "control"], "w",
             lazy.spawn("./my_scripts/webrofi.sh"),
             desc='Rofi scripts for launching websearches on firefox'
             ),
         # FZF scripts
         Key(["mod1", "control"], "i",
             lazy.spawn(myTerm+" -e sh ./my_scripts/imagefzf.sh"),
             desc='FZF scripts for opening images'
             ),
         Key(["mod1", "control"], "v",
             lazy.spawn(myTerm+" -e sh ./my_scripts/cdfzf.sh"),
             desc='FZF scripts for opening files in vim'
             ),
         # Volume
         Key([],
             "XF86AudioRaiseVolume",
             lazy.spawn("amixer -q -D pulse set Master 2%+")
             ),
         Key([],
             "XF86AudioLowerVolume",
             lazy.spawn("amixer -q -D pulse set Master 2%-")
             ),
         Key([],
             "XF86AudioMute",
             lazy.spawn("amixer -q -D pulse set Master toggle")
             ),
         # Brightness
         Key([],
             "XF86MonBrightnessUp",
             lazy.spawn("xbacklight -inc 10")
             ),
         Key([],
             "XF86MonBrightnessDown",
             lazy.spawn("xbacklight -dec 10")
             ),
         # Screenshots
         Key(["mod1", "shift"], "s",
             lazy.spawn("gnome-screenshot"),
             desc='Take screenshots'
             ),
         Key(["mod1", "control"], "s",
             lazy.spawn("gnome-screenshot -i"),
             desc='Take screenshots'
             ),
         # NWG Launchers
         Key(["mod1", "control"], "o",
             lazy.spawn("nwgbar"),
             desc='App launcher'
             ),
         Key(["mod1", "control"], "g",
             lazy.spawn("nwggrid"),
             desc='App launcher'
             ),
]

group_names = [("BROWSER"    , {'layout': 'bsp'}),
               ("EMAILS"     , {'layout': 'zoomy'}),
               ("TERMINAL"   , {'layout': 'monadtall'}),
               ("FILES"      , {'layout': 'stack'}),
               ("ZOOM"       , {'layout': 'max'}),
               ("LaTeX"      , {'layout': 'monadtall'}),
               ("MATHEMATICA", {'layout': 'monadwide'}),
               ("CHATS"      , {'layout': 'verticaltile'}),
               ("OTHERS"     , {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen())) 
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Hack Nerd Font",
         fontsize = 12,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
    layout.Floating(**layout_theme)
]

colors = ["#292d3e", # current panel background
          "#282828", # background for current screen tab
          "#ffffff", # font color for group names
          "#fb4934", # border line color for current tab
          "#8d62a9", # border line color for other tab and odd widgets
          "#668bd7", # color for the even widgets
          "#ff79c6", # window name
          "#282a36", # Main Panel
          "#6a4999", # custom widget colors 2
          "#d14a3b"] # Date & Time

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Hack Nerd Font Bold",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[7]
                       ),
              widget.TextBox(
                       text = " ",
                       font = "Hack Nerd Font",
                       fontsize = 18,
                       padding = 0,
                       foreground = colors[9],
                       background = colors[7],
                       mouse_callbacks = {
                            'Button1': lambda qtile: qtile.cmd_spawn(
                                'rofi -location 1 -yoffset 28 -xoffset 5 -show drun'
                                )
                            }
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 10,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[7],
                       other_screen_border = colors[7],
                       foreground = colors[2],
                       background = colors[7]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[7]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[7],
                       padding = 0
                       ),
              widget.Systray(
                       foreground = colors[7],
                       background = colors[7],
                       padding = 5
                       ),
              widget.TextBox(
                       text = "  ",
                       fontsize = 17,
                       foreground = colors[2],
                       background = colors[8],
                       ),
              widget.ThermalSensor(
                       fontsize = 13,
                       foreground = colors[2],
                       background = colors[8],
                       threshold = 90,
                       ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[7],
                       fontsize = 14
                       ),
              widget.Pacman(
                       update_interval = 1800,
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = colors[7]
                       ),
              widget.TextBox(
                       text = "Updates",
                       padding = 5,
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       foreground = colors[2],
                       background = colors[7]
                       ),
              widget.TextBox(
                       text = "  ",
                       foreground = colors[2],
                       background = colors[8],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[8],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
              widget.Battery(
                       full_char = "  ",
                       charge_char = "  ",
                       discharge_char = "  ",
                       foreground = colors[2],
                       background = colors[7],
                       padding = 5,
                       ),
              widget.TextBox(
                      text = " ",
                       foreground = colors[2],
                       background = colors[8],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[8],
                       get_volume_command= 'amixer -D pulse get Master'.split(), 
                       padding = 5
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[7],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[7],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[7],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[9],
                       format = "  %A, %B %d  %H:%M "
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), margin=[5, 6, 4, 6], opacity=1.0, size=22)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), margin=[5, 6, 4, 6], opacity=1.0, size=22)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), margin=[5, 6, 4, 6], opacity=1.0, size=22))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

@hook.subscribe.client_new
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()}
    for i in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()

@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, 'parent'):
        window.parent.minimized = False

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
