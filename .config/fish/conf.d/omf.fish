# Path to Oh My Fish install.
set -q XDG_DATA_HOME
  and set -gx OMF_PATH "$XDG_DATA_HOME/omf"
  or set -gx OMF_PATH "$HOME/.local/share/omf"

# Load Oh My Fish configuration.
source $OMF_PATH/init.fish

# My aliases
alias ls="lsd -ltra"
alias weather="curl wttr.in"
alias boogie="ssh boogiepop"
alias ressource="source .config/fish/conf.d/omf.fish"

# My environment variables
set -gx PATH /home/tanjona/my_scripts $PATH

# My Defs
set EDITOR "vim"
set TERM "xterm"
