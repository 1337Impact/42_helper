Black='\033[0;30m'
Red='\033[0;31m'
Green='\033[0;32m'
Yellow='\033[0;33m'  
Blue='\033[0;34m' 
Purple='\033[0;35m'
Cyan='\033[0;36m' 
White='\033[0;37m'
NC='\033[0m'

echo -en "\n    	    	            By: "
echo -e "$Red mbenkhat $NC\n"
echo -e "            $Cyan please wait a sec for installation to finish ;)"
echo -e "          if u have any problem in installation please contact me,"
echo -e "                       I'll be happy to help u;)\n $NC"

pip install -r ./42_helper/requirements.txt

echo "alias quote='python3 ~/42_helper/quote.py'
alias watchmp='python3 ~/42_helper/watch_my_post.py'
alias gwatchmp='python3 ~/42_helper/WMP_gui/main.py'
alias cluster='python3 ~/42_helper/cluster.py'" >> ~/.zshrc

echo -e "\n            $Green Command added: watchmp gwatchmp quote cluster\n"
echo -e "$Cyan Note: to be able to use watchmp please make to update ~/42_helper/config.py with your data"
echo "for more info, checkout README.md "
echo -e "\n                $Red contact me if you need help ;)$NC"
