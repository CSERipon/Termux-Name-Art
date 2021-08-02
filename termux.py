from os import system,popen
from base64 import b64encode
print("\x1b[91m")
system("clear")
system("figlet CSE RIPON")
name = input("\x1b[97m~ \x1b[92m$ Name: ")
text = b64encode(str("""
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.                                   # - Do not save duplicated commands.
shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth
echo -e "\e[91m"
clear
figlet """+name+"""
cd /sdcard/
# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '

# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi""").encode("utf-8")).decode('utf-8')
try:
	system("rm $PREFIX/etc/motd && rm $PREFIX/etc/bash.bashrc")
except:
	pass
try:
	system(f"cd $PREFIX/etc && echo {text} | base64 -d > bash.bashrc")
	print("\x1b[92m Termux Banner Name Setup Successful.")
except:
	print("\x1b[91m Termux Banner Name Setup Failed!.")