import pyodbc
# 定义一个执行 SQL 查询语句并返回结果的函数
def execute_query(sql):
    try:
        # 连接到 SQL Server 数据库
        conn = pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=Apricity;'  # 服务器名称
                              'DATABASE=testdb;'  # 数据库名称
                              'Trusted_Connection=yes')
        # 创建一个游标对象
        cursor = conn.cursor()
        # 执行 SQL 查询语句
        cursor.execute(sql)
        # 获取查询结果中的所有行
        rows = cursor.fetchall()
        # 返回查询结果
        return rows
    except Exception as e:
        # 如果出现异常，打印异常信息
        print(e)
    finally:
        # 无论是否出现异常，关闭数据库连接
        if conn:
            conn.close()

# 定义一个执行 SQL 数据操作的函数
def execute_update(sql):
    try:
        # 连接到 SQL Server 数据库
        conn = pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=Apricity;'  
                              'DATABASE=testdb;'  
                              'Trusted_Connection=yes')
        # 创建一个游标对象
        cursor = conn.cursor()
        # 执行 SQL 数据操作语句
        cursor.execute(sql)
        # 提交数据操作
        conn.commit()
        # 返回操作成功的结果
        return True
    except Exception as e:
        # 如果出现异常，打印异常信息并回滚操作
        print(e)
        conn.rollback()
    finally:
        # 无论是否出现异常，关闭数据库连接
        if conn:
            conn.close()

# 定义一个主函数来测试查询函数和数据操作函数
def main():
    # 编写 SQL 查询语句
    print("来自中国的有:")
    query = "select name2, age from TestTable where address='中国'"
    # 调用 execute_query 函数执行查询语句，并获取查询结果
    rows = execute_query(query)
    # 遍历查询结果中的所有行，并打印出姓名和年龄
    for row in rows:
        print(f"Name: {row[0]}, Age: {row[1]}")

    # 编写 SQL 数据操作语句
    update = "update TestTable set age = age + 1 where address='中国'"

    # 调用 execute_update 函数执行数据操作，并获取操作结果
    success = execute_update(update)
    # 如果操作成功，打印一个提示消息
    if success:
        print("sir，任务完成！")

# 调用主函数
if __name__ == '__main__':
    main()
