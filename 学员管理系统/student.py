# -*- codeing = utf-8 -*-
# @Time:    2021/8/27 下午 9:06
# @Author:  漫天烟华
# @Software: PyCharm
# @Version:  Python 3.9.4


class Student:
    def __init__(self, name=None, gender=None, age=None):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{self.name:<10}\t{self.gender}\t{self.age}'


if __name__ == '__main__':
    stu = Student('Dj', 'man', 19)
    print(stu.__dict__)
    print(type(stu.__dict__))