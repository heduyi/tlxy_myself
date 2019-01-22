# 推荐图书
- python编程从入门到实践

# 0. OOP - Python面向对象
- python的面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合、Mixin
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数

# 1. 面向对象的概述(ObjectOriented, OO)
- OOP思想：
    - 接触到一个任务，首先应该想到该任务由哪些模块构成
- 几个名词
    - OO:面向对象(ObjectOriented)
    - OOA:面向对象的分析(ObjectOriented analyse)
    - OOD:面向对象的设计(ObjectOriented design)
    - OOI:面向对象的实现(ObjectOriented implement)
    - OOP:面向对象的编程(ObjectOriented program)
- 面向对象的实现过程
    - OOA-->OOD-->OOI
- 类和对象的概念
    - 类：抽象的名称，代表一个集合，共性的事物。例如：学生
    - 对象：具体的事物，单个个体，一类事物中的一个个体。例如学生王小二
- 类中的内容应该包含2个内容
    - 表明事物的特征，叫属性（变量）
    - 表明事物的功能或动作，称为成员方法（函数）

# 2. 类的基本实现
- 类的命令
    - 遵守变量命名规范
    - 大驼峰
    - 避免和系统命名相同的命名
- 声明一个类
    - 必须使用class关键字
    - 类由属性(变量)和方法(函数)构成，其他的不允许出现
    - 成员的属性定义可以直接使用变量赋值，如果没有值，则使用None
    - 案例 OOP_01.py
- 实例化类
        
        变量 = 类名()  # 实例化一个对象
        
- 访问对象成员
    - 使用点操作符
        
            obj.成员属性名称
            obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
            
            # dict前后各2个下划线
            obj.__dict__
    - 类所有成员检查
            
            # dict前后各2个下划线
            class_name.__dict__
            
            
    
    
# 3. anaconda的基本使用
- anaconda主要是一个虚拟环境管理器，还是一个安装包管理器
- conda list：显示anaconda安装的包
- conda env list：显示anaconda的虚拟环境的列表
- conda create -n XXX python=3.6：创建名称为XXX，版本为python 3.6虚拟环境
    - 安装完成后使用activate oop激活名称为oop的虚拟环境(激活成功后命令行最前面会有(oop))
    - 安装完成后使用deactivate oop不激活该虚拟环境
    - test20190122 bbbbbbb