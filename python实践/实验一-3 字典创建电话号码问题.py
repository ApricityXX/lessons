#薛凡豪 20211120138 2023/3/21
ans = ""                 #空字符串，用于拼接
num = {"0":"zero","1":"one", "2":"two", "3":"three", "4":"four","5": "five","6": "six","7": "seven","8": "eight","9": "nine"}
a = input("输入你的电话号码:")      #定义字典存储对应的数字字符串和英文字母的对应关系
for i in range(len(a)):          #第一层循环：输入的电话号码的长度
    for j in num.keys():         #第二层循环：对键进行循环对比
        if(a[i]==j):
            ans = ans + num[j] + " "      #如果键和输入的相等，则拼接字典的value
print(ans)