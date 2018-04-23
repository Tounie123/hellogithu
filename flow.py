#!/usr/bin/python
# -*- coding: utf-8 -*-

# 需要安装 requests 库 :
# sudo easy_install pip
# sudo pip install requests
import requests

headers = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2454.85 Safari/537.36"
    }
    
for i in range(1, 10):
    proxies = {
        "http": "http://61.164.252.106:139"
    }
    url = "http://mp.weixin.qq.com/s/6_sfbIjJaV11Z554DNCdTA"
    print(url)
    req = requests.get(url, headers=headers, params={})
    # 设置编码
    req.encoding = 'utf-8'
    print(req.text)