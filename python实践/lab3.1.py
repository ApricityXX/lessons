def division():
    try:
        #a = float(input('请输入被除数:'))
        a=int(open("D:\\python项目\\大二python实践\\python实验三\\test2.txt","r").read())
        b = float(input('请输入除数:'))
        c = a/b
        print("the answer is {}".format(c))
    # 测试3种错误
    except(IOError, ValueError, ZeroDivisionError) as e1:   #输入输出、类型、零错误
        print("error is :{}".format(e1))
    # 测试其他错误
    except:
        print("other errors occur")
division()
