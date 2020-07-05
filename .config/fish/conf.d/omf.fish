# -- Path to Oh My Fish install ------------------------
#
set -q XDG_DATA_HOME
  and set -gx OMF_PATH "$XDG_DATA_HOME/omf"
  or set -gx OMF_PATH "$HOME/.local/share/omf"

# -- Load OMF configuration ----------------------------
#
source $OMF_PATH/init.fish

# -- Aliases -------------------------------------------
# 
# This requires `lsd`
alias ls="lsd -ltra"
alias weather="curl wttr.in"

# -- defs ----------------------------------------------
#
set EDITOR "vim"
set TERM "xterm"

# -- Budspencer color scheme ---------------------------
#
# This requires first the installation of Budspencer
# omf install budspencer
#
# omf themes are downloaded in:
# /home/<username>/.local/share/omf/themes/
set -U budspencer_colors 000000 666666 19b2ff ffffff 9066c2 ff6600 ff0000 ff0033 3300ff 0ef291 00ffff 00ff00
