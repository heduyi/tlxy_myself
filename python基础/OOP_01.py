'''
定义一个学生类，用来形容学生
'''

# 定义一个空类
class Student():
    # 一个空类，pass表示直接跳过，占位符
    pass

# 定义一个对象
dongjie = Student()


# 定义一个类，用来形容学python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'

    # def doHomework函数的缩进层级
    # 系统会默认生成一个self参数
    def doHomework(self):
        print('I am doing homework.')
        # 函数末尾使用return语句返回
        return None

# 实例化一个叫angus的学生，是一个具体的学生
angus = PythonStudent()
print(angus.name)
print(angus.age)
print(angus.course)

# 成员函数的调用没有传递参数
angus.doHomework()