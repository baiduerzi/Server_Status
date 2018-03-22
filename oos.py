# !/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib import request
import requests
from datetime import datetime

timeout = 10
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
key = 'SCKEY'
title = "上货监测"
url = ""
head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

try:
    req = request.Request(url, headers=head)
    response = request.urlopen(req, timeout=timeout)
    html = response.read()
    html = html.decode("utf-8").lower()
    str="out of stock"
    if str in html:
        print("缺货" + "\n" + time)
    else:
        print("不缺货" + "\n" + time)
        content = "上货啦~" + "\n" + time
        payload = {
            'text': title,
            'desp':content
        }
        fturl = 'https://sc.ftqq.com/{}.send'.format(key)
        requests.post(fturl, params=payload, timeout=timeout)
except Exception:
    print("Error" + "\n" + time)
