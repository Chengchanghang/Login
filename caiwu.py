# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 00:16:52 2017

@author: ChengCh
"""

import requests
import re
from bs4 import BeautifulSoup
import urllib
url = 'https://www.zhihu.com/login/phone_num'
session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

req = urllib.request.urlopen(url)
html = req.read().decode('utf-8')
get_xsrf_pattern = re.compile(r'<input type="hidden" name="_xsrf" value="(.*?)"')
lt = re.findall(get_xsrf_pattern, html)[0]

data = {
        'password':'cheng199214',
        'captcha_type':'cn',
        'phone_num':'13070847082'}
data['_xsrf'] = lt
print (data)
#login_url = 'https://cas.upc.edu.cn/cas/login'

response = session.post(url,data = data, headers = headers)
r = response.text
print (r)
