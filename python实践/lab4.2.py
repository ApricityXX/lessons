#父类
class Person:
    def __init__(self, name='', age=0, sex=''):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print(f"姓名：{self.name}，年龄：{self.age}，性别：{self.sex}")

#继承
class Student(Person):
    def __init__(self, name='', age=0, sex='', stuNo=''):
        #继承
        super().__init__(name, age, sex)
        #新增属性
        self.stuNo = stuNo
    #重写方法
    def print_info(self):
        super().print_info()
        print(f"学号：{self.stuNo}")


# 测试
student = Student(name='薛凡豪', age=20, sex='男', stuNo='20211120138')
student.print_info()

