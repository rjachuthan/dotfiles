export XDG_DATA_HOME=~/.local/share/
export XDG_CONFIG_HOME=~/.config/
export XDG_CACHE_HOME=~/.cache

export QT_QPA_PLATFORMTHEME="qt5ct"
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

export EDITOR=/usr/bin/nvim
export BROWSER=/usr/bin/librewolf
export TERMINAL=/usr/bin/kitty
export ZDOTDIR=~/.config/zsh

# Moving files out of home
export CARGO_HOME="$XDG_DATA_HOME"/cargo
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
export GOPATH="$XDG_DATA_HOME"/go
export GTK2_RC_FILES="$HOME/.config/gtkrc/gtkrc-2.0"
export IPYTHONDIR="${XDG_CONFIG_HOME}/ipython"
export JUPYTER_CONFIG_DIR="$XDG_CONFIG_HOME"/jupyter
export LESSHISTFILE="$XDG_CACHE_HOME"/less/history
export MPLAYER_HOME="$XDG_CONFIG_HOME"/mplayer
export PYTHONSTARTUP="${XDG_CONFIG_HOME}/python/pythonrc"
export WEECHAT_HOME="${XDG_CONFIG_HOME}"/weechat
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java

