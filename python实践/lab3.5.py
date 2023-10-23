import random
# 菜单
def menu():
    print("欢迎使用本抽奖系统！")
    print("-----------------")
    print('请选择你所使用的功能')
    print("1.抽奖")
    print("2.退出系统")
    print('-----------------')


def lottery_rules():
    # 获取抽奖人数以及获奖人数
    total = int(input("请输入参与抽奖的总人数："))
    first = int(input("请输入一等奖的数量："))
    second = int(input("请输入二等奖的数量："))
    third = int(input("请输入三等奖的数量："))
    # 创建存储总人数和获奖人数名单
    total_list = []
    first_list = []
    second_list = []
    third_list = []
    for x in range(total):
        total_list.append(x)
    # 获取取得一等奖的序号
    first_list = random.sample(total_list, first)
    # 删除获取过一等奖的序号，避免重复获奖
    for x in first_list:
        total_list.remove(x)
    # 获取取得二等奖的序号
    second_list = random.sample(total_list, second)
    # 删除获取过二等奖的序号，避免重复获奖
    for x in second_list:
        total_list.remove(x)
    # 获取取得三等奖的序号
    third_list = random.sample(total_list, third)
    # 删除获取过三等奖的序号，避免重复获奖
    for x in third_list:
        total_list.remove(x)
    # 打印获奖名单
    print("获取一等奖的："+str(first_list))
    print("获取二等奖的："+str(second_list))
    print("获取三等奖的："+str(third_list)+'\n')
    # 将获奖信息输入至文件
    f = open("抽奖结果.txt", "a", encoding='utf-8')
    f.write("一等奖："+str(first_list)+" 二等奖："+str(second_list)+" 三等奖："+str(third_list)+"\n")


# 主程序
def main():
    while True:
        menu()
        num = int(input())
        if num == 1:
            lottery_rules()
        elif num == 2:
            answer = input("您确定要退出系统吗？Y/N\n")
            if answer == "Y" or answer == "y":
                print("感谢您使用本系统！")
                break
            else:
                continue
        else:
            print("请输入所需功能正确的序号！\n")
            continue


main()
