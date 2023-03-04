from multiprocessing.dummy import Pool as tp
import hashlib
#  这里为已知
knownMd5 = '765db5'

def md5(text):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()

def findCode(code):   
    key = code.split(':')
    start = int(key[0])  
    end = int(key[1]) 
    for code in range(start, end):
        # 下面为截取位数
        if md5(code)[0:6] == knownMd5:            
            print(code)
            break
list=[] 
for i in range(3):    #这里的range(number)指爆破出多少结果停止
    list.append(str(10000000*i) + ':' + str(10000000*(i+1)))
pool = tp()    #使用多线程加快爆破速度
pool.map(findCode, list) 
pool.close()
pool.join()