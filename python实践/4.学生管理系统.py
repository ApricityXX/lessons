#添加add() 删除dele() 修改mul() 查询que() show()显示
import csv

def add():  #增加
    file = open("D:\\python项目\\大二python实践\\python实验二\\test4.txt","a+")
    print("输入你要增加的学生信息:( 姓名 学号 性别 手机号)")
    msg = input().split(" ")
    writeradd = csv.writer(file)
    writeradd.writerow(msg)
    print("添加成功！")
    file.close()

def dele(): #删除
    file = open("D:\\python项目\\大二python实践\\python实验二\\test4.txt","r+")
    a=[]
    print("输入你要删除的学生姓名:")
    name = input()                #name是需要删除的学生的名字
    file.readline()
    #print(file.readline()[0])
    for line in file.readlines():
        #print(line.split("\n")[1])
        if line.split(",")[0]!=name and list(line.replace(",","").split("\n")[0])!=[]:  #处理数据
            a.append(line.replace('\n',"").split(","))         #把不删除的放到一个新的列表
   # print(a[0][0])
    #print(a)
    file.close()
    file = open("D:\\python项目\\大二python实践\\python实验二\\test4.txt", "w")
    writerdele = csv.writer(file)
    writerdele.writerow(["姓名","学号","性别","手机号"])
    for i in range(len(a)):
        writerdele.writerow(a[i])              #把列表里的数据重新写入
    file.close()
    print("删除成功!")

def mul(): #修改
    file = open("D:\\python项目\\大二python实践\\python实验二\\test4.txt", "r+")
    a = []
    print("输入你要修改信息的的学生姓名:")
    name = input()  # name是需要删除的学生的名字
    file.readline()
    # print(file.readline()[0])
    for line in file.readlines():
        print(line.split("\n")[1])
        if line.split(",")[0] != name and list(line.replace(",", "").split("\n")[0]) != []:  # 处理数据
            a.append(line.replace('\n',"").split(","))  # 把不删除的放到一个新的列表
    # print(a[0][0])
    #print(a)
    file.close()
    file = open("D:\\python项目\\大二python实践\\python实验二\\test4.txt", "w")
    writerdele = csv.writer(file)
    writerdele.writerow(["姓名", "学号", "性别", "手机号"])
    for i in range(len(a)):
        writerdele.writerow(a[i])  # 把列表里的数据重新写入
    file.close()
    print("请输入修改后的信息:")
    file = open("D:\\python项目\\大二python实践\\python实验二\\test4.txt", "a+")
    msg = input().split(" ")
    writeradd = csv.writer(file)
    writeradd.writerow(msg)
    print("修改成功！")
    file.close()

def que():#查询
    file = open("D:\\python项目\\大二python实践\\python实验二\\test4.txt", "r+")
    a = []
    print("输入你要查询的学生姓名:")
    name = input()  # name是需要删除的学生的名字
    file.readline()
    # print(file.readline()[0])
    for line in file.readlines():
        print(line.split("\n")[1])
        if line.split(",")[0] == name and list(line.replace(",", "").split("\n")[0]) != []:  # 处理数据
            a.append(line)  # 把不删除的放到一个新的列表
    print("姓名   学号 性别 手机号")
    print(a[0].replace(",","  "))
def show():
    file = open("D:\\python项目\\大二python实践\\python实验二\\test4.txt", "r")
    for line in file.readlines():
        print(line.replace("\n",""))
cho=9
while cho!=0:
    print("------欢迎来到学生管理系统------")
    print("1:增加学生信息"+'\n'+"2:删除学生信息"+'\n'+"3:修改学生信息"+'\n'+"4:查询学生信息"+"\n"+"5:显示学生信息")

    cho = int(input("输入你要选择的功能：(输入0退出)"))
    if(cho==1):
        add()
    elif(cho==2):
        dele()
    elif(cho==3):
        mul()
    elif(cho==4):
        que()
    elif(cho==5):
        show()
    else:
        print("输入错误！")