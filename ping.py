#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

hostname = "baidu.com"
response = os.system("ping -c 1 "+ hostname)

#and then check the response...
if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')