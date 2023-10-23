import csv
file1 = open("D:\\python项目\\大二python实践\\python实验二\\test6.csv","w+")
sum=0
score={}
#writer = csv.writer(file1)
file1.write("姓名,性别,年龄,语文,数学,英语")
#writer.writerow(["姓名 ", "性别 ", "年龄 ", "语文成绩 ", "数学成绩 ","英语成绩"])

while True:
    line = input("请输入学生信息：（格式为“姓名 性别 年龄 语文成绩 数学成绩 英语成绩”，S结束输入）  ") #不断输入
    a = line.split(" ")
    if line.upper() == 'S':
        break
    else:
        sum += int(a[3]) + int(a[4]) + int(a[5])     #计算总分
        line.replace(" ",",")
        file1.write('\n'+line)
       # writer.writerow(line.split(' '))
        score[line] = 0
        score[line]=sum
        sum=0
newscore = sorted(score.items(),key=lambda x:x[1],reverse=True)             #排序
print(newscore)