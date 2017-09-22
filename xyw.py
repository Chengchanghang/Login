# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 00:16:52 2017

@author: ChengCh
"""

import requests
from getpass import getpass

data = {
         'service': 'default',
         'queryString': 'wlanuserip%3D172.18.187.51%26wlanacname%3D%26nasip%3D172.22.242.22%26wlanparameter%3Df4-8e-38-a8-fa-4c%26url%3Dhttp%3A%2F%2Fwww.upc.edu.cn%2F%26userlocation%3Dethtrunk%2F62%3A1305.0', 
         'operatorPwd': '', 
         'operatorUserId': '',
         'validcode': ''}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

login_url = 'http://121.251.251.207/eportal/InterFace.do?method=login'

def login(usrId,password):
    data['userId'] = userId
    data['password'] = password
    sess = requests.session()
    response = sess.post(login_url,data = data, headers = headers)
    return response.text.encode('utf-8')
if __name__ == '__main__':
    userId = input('Please input your username: ')
    password = getpass('Please input your password: ')
    print(login(userId,password))
