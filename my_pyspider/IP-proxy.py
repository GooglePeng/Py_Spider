#!/usr/bin/env python
#-*- coding:utf-8 -*- 

# Author: Occam
# Email: 15292093662@163.com
# Date: 2018-09-30
# Version: 
# Info：request测试，构建请求头


import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    headers = {'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    }
    s = requests.Session()
    req = s.get(url=url,headers=headers)
    print(s.cookies)