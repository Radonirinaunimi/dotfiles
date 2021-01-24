# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Zsh theme based on PowerLevel9K
# Tanjona R. Rabemananjara

export TERM="xterm-256color"

# Path to oh-my-zsh installation.
export ZSH="/home/tanjona/.oh-my-zsh"

# Plugins
plugins=(
  git
  git-extras
  gem
  bundler
  osx
  ruby
  rvm
  rails
  sudo
  sublime
  colorize
  history
  history-substring-search
  last-working-dir
  compleat
  virtualenv
  zsh-completions
  zsh-history-substring-search
  zsh-autosuggestions
  zsh-syntax-highlighting
)

# ZSH Themes
ZSH_THEME="powerlevel10k/powerlevel10k"
POWERLEVEL9K_MODE='nerdfont-complete'

# Configs
ENABLE_CORRECTION="true"

source $ZSH/oh-my-zsh.sh

# Paths
export PATH="/usr/lib/bin:$PATH"
# commented out by conda initialize
# export PATH="/home/tanjona/anaconda3/bin:$PATH" 
unset __conda_setup
# <<< conda initialize <<<

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='vim'
fi


# You may need to manually set your language environment
# export LANG=en_US.UTF-8
# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.

# Example aliases
alias ls="colorls -la"
alias ld="colorls -ld"
alias lt="colorls --tree"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/tanjona/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/tanjona/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/tanjona/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/tanjona/anaconda3/bin:$PATH"
    fi
fi


# Custom Functions
open() {
  vim $(fzf --preview 'bat --color "always" {}')
}

image() {
  sxiv $(fzf --preview 'bat --color "always" {}')
}

pacs() {
  sudo pacman -S $(pacman -Ssq | fzf -m --preview="pacman -Si {}" --preview-window=:hidden --bind=space:toggle-preview)
}

cdf() {
  cd $HOME && cd "$(fd -t d | fzf --preview="tree -L 1 {}" --bind="space:toggle-preview" --preview-window=:hidden)"
}

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
