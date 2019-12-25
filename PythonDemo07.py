##07-01 学习笔记

##def my_min(x, y):
##    """找最小值"""
##    print('This is my_min function')
##    res = x if x < y else y
##    return res
##
##
##def interactive():
##    print('This is interactive function')
##    user = input('user>>:').strip()
##    pwd = input('password>>:').strip()
##    return (user, pwd)
##
##print (my_min(11,12))
##
##userpwd = interactive()
##print(userpwd)
##print(type(userpwd))
##
##
##def foo():
##    print('in the foo')
##    bar()
##
##def bar():
##    print('in the bar')
##
##07-01 end

##07-02
## 形参和实参


####1.默认参数的数值通常应设为不可变类型
##def foo(n, arg=[]):
##    arg.append(n)
##    return arg
##
##print(foo(1))
##print(foo(2))
##print(foo(3))
##

####2.4 可变长度的参数(* **用法）
##def foo(x, y, z=1, *args):
##    print('this is foo')
##    print(x)
##    print(y)
##    print(z)
##    print(args)
##
##
##foo(1, 2, 3, 4, 5, 6, 7)
##
##
##def foo2(x, y, *args):
##    print('this is foo2')
##    print(x)
##    print(y)
##    print(args)
##
##
##L = [3, 4, 5]
##foo2(1, 2, *L)
##foo2(1, 2, L)
##
##
##def foo3(x, y, z=3):
##    print('this is foo3')
##    print(x)
##    print(y)
##
##
##foo3(*[1, 2])
##
##def add(*args):
##    res=0
##    for i in args:
##        res+=i
##    return res
##print("result is:")
##print(add(1,2,3,4,5,))
####2.4.2 可变长度的关键字参数
##def foo(x, **kwargs):
##    print(x)
##    print(kwargs)
##
##
##foo(y=2, x=111, z=3)
##
##
## 结果：
## 111
## {'y': 2, 'z': 3}
##def foo2(x, y, **kwargs):
##    print(x)
##    print(y)
##    print(kwargs)
##
##
##dic = {'a': 1, 'b': 2, 'c': 3}
##foo2(1, 2, **dic)
## 结果
## 1
## 2
##{'a': 1, 'b': 2, 'c': 3}


##07-04 函数对象与闭包 学习笔记
##一、函数对象
##1.1函数可以被引用
##1.2函数可以作为容器类型的元素
##1.3函数可以作为参数传入另一个函数
##1.4函数的返回值可以是一个函数
##二、闭包函数
##2.1闭与包
##2.2闭包的用途
##
## ↓↓↓↓↓↓
##
##一、函数对象
##函数对象指的是函数可以被当做'数据'来处理，具体可以分为四个方面的使用
##1.1 函数可以被引用
def add(x, y):
    return x + y
func = add
print(func(1, 2))
##>结果：3
##
##1.2 函数可以作为容器类型的元素
dic = {'add': add, 'max': max}
print(dic)
##add是我自定义的函数，max是系统的函数
##
##1.3 函数可以作为参数传入另外一个函数
def foo(x, y, func):
    return func(x,y)

print(foo(1,2,add))
##结果是3
##
##1.4 函数的返回值可以是一个函数
def bar():
    return add

func=bar()
print(func(1,2))
##结果是3， bar函数返回add函数，给func，func调用后结果为3
##
##
##二、闭包函数
##基于函数对象的概念，可以将函数返回给任意位置去调用，
##但是作用域的关系是在定义完函数时就已经被确定了的，
##与函数的调用位置无关。
##
x = 1

def f1():
    def f2():
        print(x)

    return f2

def f3():
    x = 3
    f2 = f1() #调用f1()返回函数f2
    f2() #需要按照函数定义时的作用关系去执行，与调用位置无关

print("f3（）的结果：")
f3() #结果为1
print(f1.__closure__)
print(f3.__closure__)

##也就是说，函数被当做数据处理时，始终以自带的作用域为主。
##若内嵌函数包含对外部函数作用域（而非全局作用域）中变量的引用，
##那么该'内嵌函数'就是闭包函数，简称闭包（Closures）

#比较下面一个例子
def outer():
    x=2
    def inner():
        print(x)
    return inner

func = outer()
func() #结果为2

##可以通过函数的__closure_属性，查看到闭包函数所包裹的外部变量
print("func.__closure__的内部信息↓")
print(func.__closure__)
print(func.__closure__[0].cell_contents)
print("func.__closure__的内部信息↑")
##'闭'代表函数是内部的，'包'代表函数外"包裹"着对外层作用域的引用。
##因而无论在何处调用闭包函数，使用的仍然是包裹在其外层的变量

##2.2闭包的用途
##目前为止，我们得到了两种函数传值方式，一种是直接将值以参数的形式传入
##另外一种就是将值包给函数

##2个示例比较

import requests

#方法一
def get(url):
    return requests.get(url).text


#方法二
def page(url):
    def geturl():
        return requests.get(url).text
    return geturl

##方式一下载同一个页面
#print(get('https://www.python.org'))
#print(get('https://www.python.org'))
#print(get('https://www.python.org'))

##方式二下载同一个页面
python = page('https://www.python.org')
#print(python())
#print(python())
#print(python())


##可以看出方法二在调用的时候更加方便
##闭包函数的这种特性有时又称为惰性计算。使用将值包给函数的方式，
##在接下来的装饰器中也将大有用处。

##练习：熟悉和掌握闭包函数，设定一个闭包函数，并验证
def page2(url):
    urlfix = 'https://'
    def geturl():
        return requests.get(urlfix+url).text
    return geturl

python2 = page2('www.python.org')
print(python2())
print("func.__closure__的内部信息↓")
print(python2.__closure__)
print(python2.__closure__[0].cell_contents)
print(python2.__closure__[1].cell_contents)
print("func.__closure__的内部信息↑")

##这里shenyuboqq添加的内容用来测试git获取服务上的commit号 test01 start
print("git testing by shenyuboqq")
##这里shenyuboqq添加的内容用来测试git获取服务上的commit号 test01 end
