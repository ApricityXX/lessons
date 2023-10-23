
a = open("D:\\python项目\\大二python实践\\python实验二\\test2.txt","r")  #读取文件

b = int(a.read())         #读取内容

#a = int(input())

while b>=1:    #当b>=1时，b整除2，然后输出b
    b//=2
    print(b)
a.close()