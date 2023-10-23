class Person:
    count = 0
    #初始化
    def __init__(self, name='', age=0, sex=''):
        self.__name = name
        self.age = age
        self.sex = sex
        Person.count += 1
    #用于打印实例信息
    def __str__(self):
        return f"姓名：{self.__name}，年龄：{self.age}，性别：{self.sex}"
    #使用@property装饰器提供对该属性的访问和修改
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    #实时打印当前内存中的Person对象个数
    @staticmethod
    def print_object_count():
        print(f"当前内存中的Person对象个数：{Person.count}")
    #根据特定格式的字符串实例化并返回一个Person对象
    @classmethod
    def from_string(cls, info_string):
        name, age, sex = info_string.split('，')
        age = int(age)
        return cls(name, age, sex)


# 测试
p1 = Person(name='薛凡豪', age=20, sex='男')
print(p1)  # 打印实例信息
# 输出：姓名：薛凡豪，年龄：20，性别：男

p2 = Person(age=25, sex='女')
print(p2)  # 打印实例信息
# 输出：姓名：，年龄：25，性别：女（name参数使用默认值）

p1.name = '花花'  # 修改姓名
print(p1)
# 输出：姓名：花花，年龄：20，性别：男

Person.print_object_count()  # 打印对象个数
# 输出：当前内存中的Person对象个数：2

p3 = Person.from_string("李华，22，男")  # 通过字符串实例化对象
print(p3)
# 输出：姓名：李华，年龄：22，性别：男

Person.print_object_count()  # 打印对象个数
# 输出：当前内存中的Person对象个数：3
