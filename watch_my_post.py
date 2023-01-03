#!/usr/bin/python3
import requests
import os
import json
import sys
sys.path.insert(1, './Utils')
from notify import notify, bc
from config import cookies, headers

def dict_to_arr(d_data):
    data = [] 
    for p in d_data:
        data.append(p['host'])
    return data

def post_watcher(posts):
    while (True):
        response = requests.get('https://meta.intra.42.fr/clusters.json', cookies=cookies, headers=headers)
        dict_data = json.loads(response.text)
        data = dict_to_arr(dict_data)
        for p in posts:
            if p not in data:
                return p

if (len(sys.argv) < 2):
    print(bc.FAIL, "use: watchmypost `post1` `post2` `post3 ...`\n      EX: watchmypost E2R12P2 E1R12P4", bc.ENDC)
    exit()
post = post_watcher(sys.argv[1:])
notify(post)