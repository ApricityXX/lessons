#薛凡豪 20211120138 2023/3/21
num = set()
vowels = ('a','e','i','o','u')    #元组存放元音字母
a = input("输入一段英文：")
for i in range(len(a)):          #循环字符串长度
    if(a[i] in vowels):           #判断字符是否位于vowels中
        num.add((a[i],a.count(a[i])))  #利用set去重
print(num)
#QlBQS0dJSEFTUU9XU1NOVw==
#RmFuaGFvWHVlMDNAMTYzLmNvbQ==