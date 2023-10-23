import math
import tkinter as tk
from math import *
import tkinter.messagebox as messagebox

def button_click(value):
    # 获取当前输入框中的内容
    current_expression = entry.get()
    # 清空输入框
    entry.delete(0, tk.END)
    # 将点击的按钮值添加到输入框中
    entry.insert(tk.END, current_expression + value)

def clear():
    # 清空输入框
    entry.delete(0, tk.END)

def calculate():
    # 计算结果
    result = eval(entry.get())
    # 清空输入框
    entry.delete(0, tk.END)
    # 将结果插入到输入框中
    entry.insert(tk.END, result)

def calculate_sin():
    # 计算正弦值
    result = sin(float(entry.get()))
    # 清空输入框
    entry.delete(0, tk.END)
    # 将结果插入到输入框中
    entry.insert(tk.END, result)

def calculate_cos():
    # 计算余弦值
    result = cos(float(entry.get()))
    # 清空输入框
    entry.delete(0, tk.END)
    # 将结果插入到输入框中
    entry.insert(tk.END, result)

def calculate_tan():
    # 计算正切值
    result = tan(float(entry.get()))
    # 清空输入框
    entry.delete(0, tk.END)
    # 将结果插入到输入框中
    entry.insert(tk.END, result)

#取余数计算
def calculate_modulo():
    # 获取第一个数字
    first_num = eval(entry.get())
    # 清空输入框
    entry.delete(0, tk.END)
    # 在输入框中插入第一个数字和百分号
    entry.insert(tk.END, str(first_num) + "%")
    # 绑定回车键事件，调用calculate_modulo_result函数进行计算
    window.bind('<Return>', lambda event: calculate_modulo_result(first_num))

def calculate_modulo_result(first_num):
    # 获取第二个数字
    second_num = eval(entry.get().replace("%", ""))
    # 计算取余数结果
    result = first_num % second_num
    # 清空输入框
    entry.delete(0, tk.END)
    # 将结果插入到输入框中
    entry.insert(tk.END, result)

def insert_pi():
    # 在输入框中插入π的值
    entry.insert(tk.END, str(pi))

#计算对数
def calculate_log():
    # 计算对数值
    result = log(float(entry.get()))
    # 清空输入框
    entry.delete(0, tk.END)
    # 将结果插入到输入框中
    entry.insert(tk.END, result)

#幂运算
def calculate_power():
    # 获取当前输入框中的内容
    current_expression = entry.get()
    try:
        # 尝试通过^符号拆分底数和指数
        base, exponent = current_expression.split('^')
        # 将底数和指数转换为浮点数
        base_value = float(base)
        exponent_value = float(exponent)
        # 计算幂运算结果
        result = pow(base_value, exponent_value)
        # 清空输入框
        entry.delete(0, tk.END)
        # 将结果插入到输入框中
        entry.insert(tk.END, result)
    except:
        # 若发生错误，清空输入框并显示错误信息
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")



# 帮助按钮的回调函数
def show_help():
    help_text = """
    使用帮助
    
    基本计算器操作：
    加法（+）：点击相应的按钮或使用键盘输入数字，然后点击“=”按钮以获取和。
    减法（-）：点击相应的按钮或使用键盘输入数字，然后点击“=”按钮以获取差。
    乘法（*）：点击相应的按钮或使用键盘输入数字，然后点击“=”按钮以获取乘积。
    除法（/）：点击相应的按钮或使用键盘输入数字，然后点击“=”按钮以获取商。

    高级计算器函数：
    三角函数：先输入一个数，点击“sin”、“cos”或“tan”按钮以分别计算一个数的正弦、余弦或正切值。例如0sin=0
    取模（%）：点击“%”按钮以计算两个数相除的余数。例如5%2=1
    幂运算（^）：点击“^”按钮或使用键盘输入以“^”分隔的底数和指数，以计算一个数的幂次。这里需要注意一下，这里需要类似于：5^2再点击按钮^，第一个^是键盘输入，第二个是按钮，不需要点击=按钮
    对数（log）：点击“log”按钮以计算一个数的自然对数。例如10log，这里的log运算以e为底
    圆周率（π）：点击“π”按钮以将π（3.141592653589793）的值插入输入框。
    清除（C）：点击“C”按钮以清除输入框。
    平方根(sqrt)：点击"sqrt“再输入一个括号数值可得到平方根。例如sqrt(9)=3
    附加功能：

    小数点（.）按钮：点击“.”按钮以在输入框中输入小数点。
    括号（'('，')'）按钮：点击“（”和“）”按钮以对表达式进行分组并进行相应的计算。
    帮助按钮：点击“帮助”按钮以打开一个弹出窗口，显示本用户指南。

    使用示例：
    要计算一个数的正弦值，请按照以下步骤进行：

    在输入框中输入数值。
    点击“sin”按钮。
    结果将显示在输入框中。

注意：计算器支持使用键盘输入数据
    """

    # 创建弹窗
    messagebox.showinfo("Calculator - Help", help_text)






# 创建主窗口
window = tk.Tk()
window.title("Scientific Calculator")

# 创建输入框
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# 创建按钮
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'sin', 'cos', 'tan', 'π',
    'sqrt', 'log', '(', ')',
    '%', '^', 'C','Help'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        # 创建等号按钮，点击时执行calculate函数进行计算
        tk.Button(window, text=button, width=5, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        # 创建清空按钮，点击时执行clear函数进行清空操作
        tk.Button(window, text=button, width=5, command=clear).grid(row=row, column=col)
    elif button == 'sin':
        # 创建正弦按钮，点击时执行calculate_sin函数进行计算
        tk.Button(window, text=button, width=5, command=calculate_sin).grid(row=row, column=col)
    elif button == 'cos':
        # 创建余弦按钮，点击时执行calculate_cos函数进行计算
        tk.Button(window, text=button, width=5, command=calculate_cos).grid(row=row, column=col)
    elif button == 'tan':
        # 创建正切按钮，点击时执行calculate_tan函数进行计算
        tk.Button(window, text=button, width=5, command=calculate_tan).grid(row=row, column=col)
    elif button == '%':
        # 创建取余按钮，点击时执行calculate_modulo函数进行计算
        tk.Button(window, text=button, width=5, command=calculate_modulo).grid(row=row, column=col)
    elif button == 'π':
        # 创建π按钮，点击时执行insert_pi函数插入π的值
        tk.Button(window, text=button, width=5, command=insert_pi).grid(row=row, column=col)
    elif button == 'log':
        # 创建对数按钮，点击时执行calculate_log函数进行计算
        tk.Button(window, text=button, width=5, command=calculate_log).grid(row=row, column=col)
    elif button == '^':
        # 创建幂运算按钮，点击时执行calculate_power函数进行计算
        tk.Button(window, text=button, width=5, command=calculate_power).grid(row=row, column=col)
    elif button=='Help':
        help_button = tk.Button(window, text="Help", width=5, command=show_help)
        help_button.grid(row=row, column=col)


    else:
        # 创建其他数字和运算符按钮，点击时执行button_click函数进行操作
        tk.Button(window, text=button, width=5, command=lambda value=button: button_click(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 运行主循环
window.mainloop()
