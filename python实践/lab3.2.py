def openfile():
    try:
        # 输入文件路径并尝试打开文件
        add = input("请输入所要打开的文件路径：")
        f = open(add, 'r', encoding='utf-8')
        print(f.read())
        f.close()
        # 对文件路径不正确错误进行异常处理，反复调用直至输入正确或出现其他错误
    except (FileNotFoundError, PermissionError):
        print("文件路径不正确，请重新输入。")
        openfile()
    except UnicodeDecodeError as e1:
        print(e1)
    except:
        print('出现其他错误，请仔细检查')
    else:
        f.close()

openfile()
