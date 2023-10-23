import os
#订单文件
filename = 'orders.txt'
#文件是否存在
if os.path.exists(filename):
    with open(filename, 'r') as f:
        content = f.read()
    orders = eval(content)
else:
    orders = {}
#输入信息
table_num = input("请输入桌号：")
dish_name = input("请输入餐品名称：")
dish_num = int(input("请输入份数："))
#如果这一桌已经在订单里
if table_num in orders:
    if dish_name in orders[table_num]:     #如果已经点过这份菜，直接加数量即可
        orders[table_num][dish_name] += dish_num
    else:                                  #如果没点这份菜
        orders[table_num][dish_name] = dish_num
else:                                      #如果还没点菜
    orders[table_num] = {dish_name: dish_num}
#写入订单
with open(filename, 'w') as f:
    f.write(str(orders))
#读取订单
with open(filename, 'r') as f:
    content = f.read()
#eval()转列表
orders = eval(content)
#打印
for table_num, items in orders.items():
    print(f"桌号：{table_num}")
    for dish_name, dish_num in items.items():
        print(f"{dish_name}x{dish_num}")
    print("=" * 10)
