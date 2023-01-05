Black='\033[0;30m'
Red='\033[0;31m'
Green='\033[0;32m'
Yellow='\033[0;33m'  
Blue='\033[0;34m' 
Purple='\033[0;35m'
Cyan='\033[0;36m' 
White='\033[0;37m'
NC='\033[0m'

#get the shell configuration file name
shell_f=$(echo -n "$SHELL" | awk -F / '{print $3}')
shell_f="${HOME}/.${shell_f}rc"

echo -en "\n    	    	            By: "
echo -e "$Red mbenkhat $NC\n"
echo -e "            $Cyan please wait a sec for installation to finish ;)"
echo -e "          if u have any problem in installation please contact me,"
echo -e "                       I'll be happy to help u;)\n $NC"

pip install -r ./42_helper/requirements.txt

#test if commands are already installed
if grep "alias quote='python3 ~/42_helper/quote.py'" <"$shell_f" &>/dev/null \
&& grep "alias watchmp='python3 ~/42_helper/watch_my_post.py'" <"$shell_f" &>/dev/null \
&& grep "alias gwatchmp='python3 ~/42_helper/WMP_gui/main.py'" <"$shell_f" &>/dev/null \
&& grep "alias cluster='python3 ~/42_helper/cluster.py'" <"$shell_f" &>/dev/null;
then
	sleep 0.5
else
	sleep 0.5
	echo "alias cclean='python3 ~/42_helper/optimized_cclean.py'
alias quote='python3 ~/42_helper/quote.py'
alias watchmp='python3 ~/42_helper/watch_my_post.py'
alias gwatchmp='python3 ~/42_helper/WMP_gui/main.py'
alias cluster='python3 ~/42_helper/cluster.py'" >> $shell_f
fi

echo -e "\n            $Green Command added: watchmp gwatchmp quote cluster cclean\n"
echo -e "$Cyan Note: to be able to use watchmp please make to update ~/42_helper/config.py with your data"
echo "for more info, checkout README.md "
echo -e "\n                $Red contact me if you need help ;)$NC"
zsh
