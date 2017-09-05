#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

reset=$(tput sgr0)
bold=$(tput bold)
black=$(tput setaf 0)
red=$(tput setaf 1)
green=$(tput setaf 2)
yellow=$(tput setaf 3)
blue=$(tput setaf 4)
magenta=$(tput setaf 5)
cyan=$(tput setaf 6)
white=$(tput setaf 7)

alias la='ls -la'
alias ls='ls --color=auto'

export PS1='\[${reset}${bold}\]\[\] \[${reset}${bold}\]\u@\h\[${reset}${bold}\] in\[${reset}${bold}\] \W \[${green}\]\[\] \[${reset}\]' 
