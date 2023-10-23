class Animal:
    def make_sound(self):
        print("动物叫")


class Dog(Animal):
    def make_sound(self):
        print("狗汪汪")


class Cat(Animal):
    def make_sound(self):
        print("猫喵喵")

#继承两个类
class DogCat(Cat, Dog):
    #空语句
    pass

#测试
dog_cat = DogCat()
dog_cat.make_sound()
