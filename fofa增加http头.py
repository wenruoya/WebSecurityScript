import sys
import getopt

def  file(file_name):
    f = open(file_name, mode = 'r')
    for con in f:
        if ('http://' or 'https://') not in con:
            if con.isspace():
                continue
            else:
                tmp = 'http://'+ con
            with open('result.txt','a',encoding='utf-8') as output :
                output.writelines(tmp) 
        else:
            continue
    f.close()



if __name__ == '__main__':
    print('用法:-f --file_name  文件名')
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "h:f:",
                                   ["help",
                                    "file_name"])
    except:
        print("Error")

    for opt, arg in opts:

        if opt in ['-f', '--file_name']:
            file(arg) 