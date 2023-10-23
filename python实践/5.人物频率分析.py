#预处理数据和文件 字典赋予需要查询的名字
names1 = {"斯嘉丽":0,"白瑞德":0,"艾希利":0,"查尔斯":0,"斯图尔特":0,"布伦特":0,"博伊德":0,"林肯":0,"塔尔顿":0,"威尔克斯":0,"奥哈拉":0,'波密尔顿':0,"汉密尔顿":0,"媚兰":0,"弗兰克":0,"贝尔":0}
names2 = {"Scarlett":0,"Rhett":0,"Ashley":0,"Melanie":0,"Gerald":0,"Ellen":0,"Suellen":0,"Carreen":0,"Charles":0,"Frank":0,"Pitty":0,'Belle':0,"Wade":0,"Ella":0}
file1 = open("D:\\python项目\\大二python实践\\python实验二\\飘_中文版.txt","r",encoding="utf-8")   #读文件
file2 = open("D:\\python项目\\大二python实践\\python实验二\\飘_英文版.txt","r",encoding="utf-8")
text1 = file1.read()    #text为读取内容变量
text2 = file2.read()
#对中文处理
for i in names1:         #遍历字典
    if i in text1:         #判断是否在文章中
        names1[i]+=text1.count(i)   #统计次数
new_names1 = sorted(names1.items(),key=lambda x:x[1],reverse=True) #排序，按照键值降序
print("中文版的检测结果:")
print("名字-------次数")
for i in range(10):
    print("{0:<10}{1:>4}".format(new_names1[i][0],new_names1[i][1]))      #输出元组的前两项

#对英文处理
for i in names2:
    if i in text2:                    #和上面相同
        names2[i]+=text2.count(i)
new_names2 = sorted(names2.items(),key=lambda x:x[1],reverse=True)
print("\nThe detection result for an English version:")
print("name-------number")
for i in range(10):
    print("{0:<10}{1:>5}".format(new_names2[i][0],new_names2[i][1]))

file1.close()
file2.close()