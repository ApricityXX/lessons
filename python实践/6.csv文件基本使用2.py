file1 = open("D:\\python项目\\大二python实践\\python实验二\\test6.csv","r")
score={}
file1.readline()
for line in file1.readlines():
    score[line]=0
    a=line.split(" ")

    score[line]=int(a[3])+int(a[4])+int(a[5])           #总分

newscore = sorted(score.items(),key=lambda x:x[1],reverse=True)    #按照总分排序

file2 = open("D:\\python项目\\大二python实践\\python实验二\\test6.2.csv","w")
file2.write("姓名 性别 年龄 语文 数学 英语")
for i in range(len(newscore)):
    str1 = str(newscore[i][0].replace('\n',""))+" "+str(newscore[i][1])
    file2.write('\n')
    file2.write(str1)                            #写入文件test6.2.csv
    print(str1)
    str1=""




