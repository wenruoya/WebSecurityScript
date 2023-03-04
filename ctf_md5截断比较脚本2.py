import hashlib

for i in range(1, 10000001):
    # 截断位数
    s = hashlib.md5(str(i)).hexdigest()[0:6]
    # 已知
    if s == "f3ff5e":
        print(i)
        break