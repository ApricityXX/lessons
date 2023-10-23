#薛凡豪 20211120138 2023/3/21
a=[]                          #建立一个空列表a
for i in range(10000):      #循环从0-9999
    flag=True               #定义标记flag=true
    b=i%7                   #把除以7余数为零放到第一层循环，降低时间复杂度，提高效率
    for j in range(2,7):
        if(i%j!=j-1 or b!=0):  #这个循环体即判断是否符合题目的余数要求，如果有一项不符合，那么flag=false，反之，flag仍然为true
            flag=False
    if(flag):
        a.append(i)              #如果flag=true，则加入到列表
print(a)                        #输出
print("最小的是：",a[0])
