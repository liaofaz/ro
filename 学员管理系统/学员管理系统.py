# -*- codeing = utf-8 -*-
# @Time:    2021/8/27 下午 8:45
# @Author:  漫天烟华
# @Software: PyCharm
# @Version:  Python 3.9.4


from student import Student
import json


class StudentManagerSystem:
    def __init__(self):
        self.students = {}

    def menu(self):
        print('-'*25)
        print(f'{"* 欢迎使用学院管理系统 *":^20}\n')
        print('   1. 添加学员')
        print('   2. 删除学员')
        print('   3. 修改学员')
        print('   4. 查询学员信息')
        print('   5. 显示所有学员信息')
        print('   6. 退出系统')
        print('-'*25)

    def run(self):
        self.systeam_init()
        while True:
            # 1.功能界面
            self.menu()
            menu = input('请输入功能序号，选择您需要的服务:')
            print()
            if not menu.isdigit() or int(menu) < 1 or int(menu) > 6:
                print('-'*25)
                print('错误输入！！！请重新输入！！！')
                continue
            menu = int(menu)
            if menu == 1:
                self.add_student()
            elif menu == 2:
                self.del_student()
            elif menu == 3:
                self.modify_student()
            elif menu == 4:
                self.seach_student()
            elif menu == 5:
                self.show_student()
            else:
                print('系统退出成功，期待您的再次使用~')
                self.save_stu()
                break

    def systeam_init(self):
        try:
            f = open('student.data')
            print('数据加载中...')
        except:
            f = open('student.data', 'w')
            print('数据文件新建成功...')
        data = f.read()
        if data:
            data = eval(data)
            f.close()
            self.students = {i: Student(j['name'], j['gender'], j['age']) for i, j in data.items()}

    def add_student(self):
        s_id = input('请输入学号:')
        name = input('请输入学生姓名:')
        gender = input('请输入性别:')
        age = input('请输入年龄:')
        self.students[s_id] = Student(name, gender, age)
        print('添加成功:')
        print(s_id, self.students[s_id])

    def del_student(self):
        s_id = input('请输入要删除的学员的学号:')
        find = self.students.get(s_id)
        if find:
            del self.students[s_id]
            print(s_id, find)
            print('该信息已删除成功✓')
        else:
            print('该学员不存在！')

    def modify_student(self):
        s_id = input('请输入需要修改的学员的学号:')
        find = self.students.get(s_id)
        if find:
            print(find)
            name = input('请输入新的学生姓名:')
            gender = input('请输入性别:')
            age = input('请输入年龄:')
            self.students[s_id] = Student(name, gender, age)
            print('信息修改成功✓')
        else:
            print('该学员不存在')

    def seach_student(self):
        s_id = input('请输入需要查询的学员的学号:')
        find = self.students.get(s_id)
        if find:
            print(f'{"学号"}\t{"姓名":<10}\t{"性别"}\t{"年龄"}')
            print(s_id, find)
        else:
            print('该学员不存在')

    def show_student(self):
        if not self.students:
            print('学员空空如也...')
            return
        print(f'{"学号"}\t{"姓名":<10}\t{"性别"}\t{"年龄"}')
        for i, j in self.students.items():
            print(i, j)

    def save_stu(self):
        with open('student.data', 'w') as f:
            stu_dict = {i: j.__dict__ for i, j in self.students.items()}
            f.write(str(stu_dict))


if __name__ == '__main__':
    student = StudentManagerSystem()
    student.run()
