export TERM="xterm-256color"

# History
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zsh/history

# Some useful options (man zshoptions)
setopt autocd extendedglob nomatch menucomplete
setopt interactive_comments
zle_highlight=('paste:none')

# Remove Beep
unsetopt BEEP

# Prompt Settings
declare -a PROMPTS
PROMPTS=(
    "∮"
    "∯"
    "≎"
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
)
# RANDOM=$$$(date +%s)
# ignition=${PROMPTS[$RANDOM % ${#RANDOM[*]}+1]}
PROMPT='%F{yellow}%1~%f %F{green} %f '

## Git Settings
autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst
RPROMPT=\$vcs_info_msg_0_
zstyle ':vcs_info:git:*' formats '%F{yellow}(%b)%r%f'
zstyle ':vcs_info:*' enable git

# Completion
autoload -Uz compinit && compinit #need the next two lines for case insensitive tab completion
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'

# autoload -Uz compinit
# zstyle ':completion:*' menu select
# zmodload zsh/complist
# _comp_options+=(globdots)

autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

# Colors
autoload -Uz colors && colors



# Keybindings
bindkey -v # vi-mode
bindkey -s '^o' 'ranger^M'
bindkey '^p' up-line-or-beginning-search
bindkey '^n' down-line-or-beginning-search
bindkey '^k' up-line-or-beginning-search
bindkey '^j' down-line-or-beginning-search



# Executable Paths
export EDITOR="nvim"
export PATH=$PATH:~/scripts
export PATH=$PATH:~/.emacs.d/bin
export PATH=$PATH:~/.miniconda/bin



# Aliases
alias vim="nvim"
export ZSHPATH="~/.config/zsh/.zshrc"

alias ei3="$EDITOR ~/.i3/config"
alias equte="$EDITOR ~/.config/qutebrowser/config.py"
alias evi="$EDITOR ~/.config/nvim/init.lua"
alias epicom="$EDITOR ~/.config/picom.conf"
alias ezsh="$EDITOR $ZSHPATH"
alias szsh="source $ZSHPATH"

alias grep="grep --color=auto"
alias ls='exa --icons --group-directories-first --color auto'

alias obclip="mv ~/Downloads/Markdown/* ~/Documents/ZettelNotes/05\ Clippings"
alias obfood="mv ~/Downloads/Markdown/* ~/Documents/ZettelNotes/05\ Clippings/Food"
alias zet="cd ~/Documents/ZettelNotes;git status"
alias hn="hackernews_tui --config ~/.config/hn-tui.toml"

alias anime="sh ~/Codes/GH_Projects/ani-cli/ani-cli"

alias clearswap="sudo swapoff -a && sudo swapon -a"
alias clearsystem="~/scripts/system-maintenance.sh"

# Confirm before overwriting something
alias cp="cp -i"
# alias mv="mv -i"
# alias rm="rm -i"





# ####################################################################################
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/rituraj/.miniconda/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/rituraj/.miniconda/etc/profile.d/conda.sh" ]; then
        . "/home/rituraj/.miniconda/etc/profile.d/conda.sh"
    else
        export PATH="/home/rituraj/.miniconda/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
# ####################################################################################

ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}
