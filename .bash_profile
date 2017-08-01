# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi

# User specific environment and startup programs

# easy file backup command
function backup() {
  newname=$1.`date +%Y%m%d.%H%M.bak`;
  mv $1 $newname;
  echo "Backed up $1 to $newname.";
  cp -p $newname $1;
}

# store entire bash history
export PROMPT_COMMAND='if [ "$(id -u)" -ne 0 ]; then echo "$(date "+%Y-%m-%d.%H:%M:%S") $(pwd) $(history 1)" >> ~/.logs/bash-history-$(date "+%Y-%m-%d").log; fi'

# set python3 as default
alias python=python3

# set pip3 as default
alias pip=pip3
