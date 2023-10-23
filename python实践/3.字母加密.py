#薛凡豪 20211120138 2023/3/28
file1 = open("test3.txt", "r")      #读文件
str1 = file1.read()                #把原始内容赋值给str1
str2=""                            #str2存储加密后的字符串
for i in range(len(str1)):
    if (ord(str1[i])>=65 and ord(str1[i])<90) or  (ord(str1[i])>=97 and ord(str1[i])<122):  #A-Y,a-y
        str2+=chr(ord(str1[i])+1)
    elif ord(str1[i])==90 or ord(str1[i])==122:         #Z或者z
        str2+=chr(ord(str1[i])-25)
    else:                                             #其余的不变
        str2+=str1[i]
print("加密之前的字符串：",str1)
print("加密之后的字符串：",str2)
file1.close()