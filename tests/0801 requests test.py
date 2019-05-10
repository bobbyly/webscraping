# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 08:15:32 2019

@author: bly6
"""

import requests

oxxstudio = input('you know what it is: ')

proxies = {
  'http': 'http://bly6:'+oxxstudio+'@httpgw.kmtltd.net.au:8080',
  'https': 'HTTPS_PROXY=http://bly6:'+oxxstudio+'@httpgw.kmtltd.net.au:8080',
}

response = requests.get('http://api.open-notify.org/iss-now.json', 
                        proxies=proxies )
try:
    print(response.status_code)
except Exception as e:
    print (type(e))
    print (e)
