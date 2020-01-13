## 元类

## 一、元类介绍
# 什么是元类？
class StandfordTeacher(object):
    school = 'Stanford'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print('%s says welcom to the Stanford to learn Python' %self.name)

#sample 01
t1 = StandfordTeacher('lili',18)
print(type(t1))
## 查看对象t1的类是<class '__main__.StandfordTeacher'>
## 如果一切皆为对象，那么类StanfordTeacher本质也是一个对象，
## 既然所有的对象都是调用类得到的，那么，StandfordTeacher必然也是调用了一个类得到的，
## 这个类称为元类

## 于是，我们推导出 --> 产生StanfordTeacher的过程一定发生了：StanfordTeacher=元类(...)
print(type(StandfordTeacher))
## 结果为<class 'type'>，证明是调用了type这个元类而产生的StanfordTeacher，
## 即默认的元类为type

# 二、class关键字创建类的流程分析
# 上文我们基于python中一切皆为对象的概念分析出：我们用class关键字定义的类本身也是一个对象
# 负责产生该对象的类称为元类（简称为类的类），内置的元类为type
# class关键字在帮我们创建类的时候，必然帮我们调用了元类StanfordTeacher=type(...)，
# 那调用type时，传入的参数分别是：
# 1.类名class_name='StanfordTeacher'
# 2.基类们class_bases=(object,)
# 3.类的名称空间 class_dic，类的名称空间是执行类体代码而得到的
# 调用type时会依次传入以上三个参数。
# 综上，class关键字帮我们创建一个类，应该细分为以下四个过程。
# 1.拿到类名
# 2.拿到类的基类们
# 3.执行类体代码，拿到类的名称空间：class_dic={...}
# 4.调用元类得到类：StanfordTeacher=type(class_name,class_bases,class_dic)
#
# 补充 exec的用法
# 参数1：包含一系列python代码的字符串
# 参数2：全局作用域（字典形式），如果不指定，默认为globals()
# 参数3：局部作用域（字典形式），如果不指定，默认为locals()
# 可以把exec命令的执行当成是一个函数的执行，会将执行期间产生的名字存放于局部名称空间中
#
# ，

# sample02
print("sample 02 start....")
g={
    'X':1,
    'y':2
}

l={}

exec('''
global x,z
x=100
z=200

m=300
''',g,l)

print("------------------")
print(g)
print("-------------------")
print(l)
