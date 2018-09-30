#!/usr/bin/env python
#-*- coding:utf-8 -*- 

# Author: Occam
# Email: 15292093662@163.com
# Date: 2018-09-30
# Version: 
# Info：测试selenium环境，前提是下载了firefox的driver,并将便携版firefox添加到了系统环境变量


'''
# 基于Firefox
from selenium import webdriver

dr = webdriver.Firefox()
dr.get('https://www.sogou.com')
dr.close()
'''

# 基于360chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
 
browser_url = r'E:\Software\浏览器\360Chrome\Application\360chrome.exe'
chrome_options = Options()
chrome_options.binary_location = browser_url
 
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.sogou.com')
# driver.find_element_by_id("kw").send_keys("seleniumhq" + Keys.RETURN) 为什么要加这句话？不加的话终端进程不会退出，还有疑问！
time.sleep(5)
driver.quit()
# 亲测可用