import csv
import re
with open('s.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    flag = {}
    res = ""
    for row in reader:
        if int(row[0]) >= 627:
            r = re.findall(".*%s(.*)%s.*" % ("%20", ",%201"), row[7])
            c = re.findall(".*%201\)\)>(.*) HTTP/1.1.*", row[7])
            # print(r[0]+":"+chr(int(c[0])))
            flag[r[0]] = c[0]
            # print(flag)
    for key in flag:
        res += chr(int(flag[key]))
    print(res)