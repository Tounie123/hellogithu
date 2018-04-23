#!/usr/bin/python
# -*- coding: utf-8 -*-

# 需要安装 requests 库 :
# sudo easy_install pip
# sudo pip install requests
import requests


for i in range(1, 10):
    proxies = {
        "http": "http://61.164.252.106:139"
    }
    url = "https://blog.csdn.net/zhoutuan1/article/details/51965644"
    #print(url)
    req = requests.get(url)
    # 设置编码
    req.encoding = 'utf-8'
    print(req.text)