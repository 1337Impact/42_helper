import requests
import json

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = "https://api.quotable.io/random"

response = requests.request("GET", url)
data = json.loads(response.text)
print(bc.OKCYAN , data['content'], bc.ENDC)
for e in range(data["length"] - len(data['author'])):
    print(" ", end='')
print(bc.FAIL , "by:", data['author'], bc.ENDC)
