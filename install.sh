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

pip install -r requirements.txt

echo "alias quote='python3 ~/the_usefull_app/quote.py'
alias watchmp='python3 ~/the_usefull_app/quote.py'
alias cluster='python3 ~/the_usefull_app/cluster.py'" >> ~/.zshrc

echo -e "\n            $Green Command added: quote watchmp cluster\n"
echo -e "$Cyan Note: to be able to use watchmp please make to update config.py with your data"
echo "for more info, read README.md "
echo -e "\n                $Red contact me if you need help ;)$NC"
