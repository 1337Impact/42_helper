import requests
import json
import sys
import os
sys.path.insert(1, os.path.dirname(__file__)+'/../Utils')
from notify import notify
from msg_sender import send_message

from config import cookies, headers
def dict_to_arr(d_data):
    data = []
    for p in d_data:
        data.append(p['host'])
    return data

def post_watcher(posts, msg):
    while (True):
        response = requests.get('https://meta.intra.42.fr/clusters.json', cookies=cookies, headers=headers)
        dict_data = json.loads(response.text)
        data = dict_to_arr(dict_data)
        for p in posts:
            if p not in data:
                if msg == "on":
                    send_message(p)
                    print("msg send")
                notify(p)
                posts.remove(p)
                if len(posts) == 0:
                    return p
