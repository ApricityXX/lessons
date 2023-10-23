import sys
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
s = a+b+c           #定义三个相加，字符串

print(s)   #标准输出
sys.stdout = open("D:\\python项目\\大二python实践\\python实验二\\test1.txt","a")   #保存在文本文件
f = open("D:\\python项目\\大二python实践\\python实验二\\test1.txt","r")
print(s)   #输出到文件
sys.stdout = sys.__stdout__     #标准输出
