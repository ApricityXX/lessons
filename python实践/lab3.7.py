def info_start():
    print('欢迎使用本学生信息管理系统！--------------')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.显示学生信息')
    print('5.输出某个学生成绩明细')
    print('6.输出某个学生成绩排名')
    print('7.退出系统')


def info_add():
    """"添加学生信息"""
    # 接受用户输入的学生信息
    new_name = input('请输入该学生的姓名:')
    new_sex = input('请输入该学生的性别:')
    new_num = input('请输入该学生的学号:')
    new_chinese = int(input('请输入该学生语文成绩'))
    new_math = int(input('请输入该学生数学成绩'))
    new_english = int(input('请输入该学生英语成绩'))

    info_dict={}
    info_dict['name'] = new_name
    info_dict['sex'] = new_sex
    info_dict['num'] = new_num
    info_dict['chinese'] = new_chinese
    info_dict['math'] = new_math
    info_dict['english'] = new_english
    info = []
    info.append(info_dict)
    file = open('学生信息.txt', 'a+', encoding='utf-8')
    for x in info:
        file.write(str(x)+',')
    file.close()
    print('添加成功！')


def info_del():
    """"删除学生信息"""
    # 接受用户输入的想要删除的学生的姓名
    del_name = input('请输入你想要删除的学生的姓名')
    file = open('学生信息.txt', 'r', encoding='utf-8')
    info = list(eval(file.read()))
    file.close()
    for x in info:
        if x['name'] == del_name:
            info.remove(x)
            print('删除成功！')
        else:
            print('你输入的学生不存在！')
    file = open('学生信息.txt', 'w', encoding='utf-8')
    for x in info:
        file.write(str(x)+',')
    file.close()


def info_modify():
    """"修改学生信息"""
    # 用户输入想修改学生的姓名
    modify_name = input('请输入要修改学生的姓名：')
    file = open('学生信息.txt', 'r', encoding='utf-8')
    info = list(eval(file.read()))
    file.close()
    for x in info:
        if x['name'] == modify_name:
            new_sex = input('请输入修改后的学生的性别:')
            new_num = input('请输入修改后的学生的学号:')
            new_chinese = int(input('请输入修改后的语文成绩'))
            new_math = int(input('请输入修改后的数学成绩'))
            new_english = int(input('请输入修改后的英语成绩'))
            x['sex'] = new_sex
            x['num'] = new_num
            x['chinese'] = new_chinese
            x['math'] = new_math
            x['english'] = new_english
            print('修改成功！')
            break
    else:
        print('你输入的学生不存在！')
    file = open('学生信息.txt', 'w', encoding='utf-8')
    for x in info:
        file.write(str(x)+',')
    file.close()


def info_show():
    """"显示学生信息"""
    file = open('学生信息.txt', 'r', encoding='utf-8')
    print(file.read())
    file.close()


def info_grade():
    """"查询单个学生所有成绩"""
    file = open('学生信息.txt', 'r', encoding='utf-8')
    info = list(eval(file.read()))
    file.close()
    name = input('请输入查询学生的姓名')
    for x in info:
        if x['name'] == name:
            if x['chinese'] != 0 and x['math'] != 0 and x['english'] != 0:
                print("所需查询的学生信息及成绩存在！")
                print('该学生的语文成绩：' + str(x['chinese']) + '，数学成绩：' + str(x['math']) + '，英语成绩：' + str(x['english']))
                break
            if x['chinese'] == 0 or x['math'] == 0 or x['english'] == 0:
                print("所需查询的学生成绩不存在！")
                break
    else:
        print('你输入的学生不存在！')


def info_ranking():
    name = input('请输入想要查询学生的姓名')

    # 遍历列表得到学生语文成绩
    def get_chinese_rank():
        m = 1
        chinese_rank = []
        file = open('学生信息.txt', 'r', encoding='utf-8')
        info = list(eval(file.read()))
        file.close()
        # 创建一个列表存储语文成绩排名
        for x in info[:]:
            m += 1
            chinese_rank.append({'name': x['name'], 'chinese': x['chinese']})
        new_chinese_rank = sorted(chinese_rank, key=lambda ch: ch.get('chinese'), reverse=True)
        # 遍历存储语文成绩排名的列表获取排名
        for x in info[:]:
            m += 1
            if x['name'] == name:
                for count in range(len(new_chinese_rank)):
                    if new_chinese_rank[count]['name'] == x['name']:
                        count += 1
                        print('语文排名'+str(count))

    # 遍历列表得到学生数学成绩
    def get_math_rank():
        m = 1
        math_rank = []
        file = open('学生信息.txt', 'r', encoding='utf-8')
        info = list(eval(file.read()))
        file.close()
        # 创建一个列表存储数学成绩排名
        for x in info[:]:
            m += 1
            math_rank.append({'name': x['name'], 'math': x['math']})
            new_math_rank = sorted(math_rank, key=lambda ch: ch.get('math'), reverse=True)
            # 遍历存储数学成绩排名的列表获取排名
        for x in info[:]:
            m += 1
            if x['name'] == name:
                for count in range(len(new_math_rank)):
                    if new_math_rank[count]['name'] == x['name']:
                        count += 1
                        print('数学排名' + str(count))

    # 遍历列表得到学生英语成绩
    def get_english_rank():
        m = 1
        english_rank = []
        file = open('学生信息.txt', 'r', encoding='utf-8')
        info = list(eval(file.read()))
        file.close()
        # 创建一个列表存储英语成绩排名
        for x in info[:]:
            m += 1
            english_rank.append({'name': x['name'], 'english': x['english']})
        new_english_rank = sorted(english_rank, key=lambda en: en.get('english'), reverse=True)
        # 遍历存储英语成绩排名的列表获取排名
        for x in info[:]:
            m += 1
            if x['name'] == name:
                for count in range(len(new_english_rank)):
                    if new_english_rank[count]['name'] == x['name']:
                        count += 1
                        print('英语排名' + str(count))

    get_chinese_rank()
    get_math_rank()
    get_english_rank()


def main():
    while True:
        info_start()
        x = int(input('请输入你想选择的功能的序号:'))
        if x == 1:
            info_add()
        elif x == 2:
            info_del()
        elif x == 3:
            info_modify()
        elif x == 4:
            info_show()
        elif x == 5:
            info_grade()
        elif x == 6:
            info_ranking()
        elif x == 7:
            print('成功退出，欢迎您下次使用本系统！')
            break
        else:
            print('你输入的序号有误，请重新输入！')


main()
