#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
from datetime import datetime

timeout = 10
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

key = 'SCU20211T5a48f0049a7d4bff618c5b4c0eba8a515a5d822ca1dfe'

title = "VPS在线检测"
#content = "The VPS is running 7"


hostname = "pa.ci"
response = os.system("ping -c 1 "+ hostname)

#and then check the response...
if response == 0:
    content = "The vps is up"
#    print(hostname, 'is up!')
else:
    content = "The vps is down"
#    print(hostname, 'is down!')


payload = {
    'text': title,
    'desp': content + "  " + time
}

url = 'https://sc.ftqq.com/{}.send'.format(key)
requests.post(url, params=payload, timeout=timeout)