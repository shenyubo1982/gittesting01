# coding:utf-8
###
#07-07 生成器
#一、生成器与yield
#若函数体包含yield关键字，再调用函数，并不会执行函数体代码，得到的返回值即生成器对象

## sample 01
def my_range(start,stop,step=1):
    print("start...")
    while start < stop:
        yield start
        start+=step
    print("end...")

g=my_range(0,3)
##print(g)  # >> <generator object my_range at 0x1063e4a20>

#生成器内置有__iter__和__next__方法，所以生成器本身也是一个迭代器
##print(g.__iter__)
##print(g.__next__)
##因而我们可以用next（生成器）触发生成器所对应函数的执行，
##print(next(g))  #触发函数执行知道遇到yield则停止，将yield后的值返回，并在当前位置挂起函数
##print(next(g))  #再次调用next(g)，函数从上次暂停的位置继续执行，知道重新遇到yield
##print(next(g))  #周而复始。。。
##print(next(g))  #触发函数执行没有遇到yield则无值返回，即取物完毕抛出异常结束迭代

#既然生成器对象属于迭代器，那么必然可以使用for循环迭代，如下：
for i in g:
    print(i)

#有了yield关键字,我们就有了一种自定义迭代器的实现方式。yield可以用于返回值，
#但不同于return，函数一旦遇到return就结束了，而yield可以保存函数的运行状态挂起函数
#用来返回多次值



##二、yield表达式应用
## 在函数内可以采用表达式形式的yield
## sample 02
def eater():
    print('1.Ready to eat')
    while True:
        food = yield
        print('1.get the food: %s, and start to eat' %food)

g=eater() #得到生成器对象
print(g)
next(g)   #需要实现"初始化"一次，让函数挂起在food=yield，等待调用g.send()方法为其传值
g.send('包子')
g.send('鸡腿')
#针对表达式形式的yield，生成器对象必须事先先辈初始化一次，让函数挂起在food=yield的位置，
##等待调用g.send()方法为函数体传值，g.send(None)等同于next(g)


##我们可以编写装饰器来完成为所有表达式形式yield对应生成器的初始化操作，如下：
# sample 03
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        return g
    return wrapper

@init
def eater():
    print('2.Ready to eat')
    food_list=[]
    while True:
        food = yield food_list ##表达式形式的yield也可以用于返回多次值 【变量名=yield 值】的形式
        food_list.append(food)
        print('2.get the food: %s, and start to eat' %food_list)


e=eater()
next(e)
e.send('蒸羊羔')
e.send('蒸熊掌')
e.send('蒸鱼翅')


##三、三元表达式、列表生成式、生成器表达式
#3.1三元表达式
#三元表达式是python为我们提供的一种简化代码解决方案，语法如下：
#res= 条件成立时返回的值 if 条件 else 条件不成立时返回的值
#sample 04
def max2(x,y):
    if x > y:
        return x
    else:
        return y

res = max2(1,2)
print(res)

## sample 04
# 三元表达式可以一行解决
x=4
y=5
res= x if x>y else y
print(res)

##3.2 列表生成式
# 列表生成式是python为我们提供的一种简化代码的方案，用来快速生成列表，语法如下

##[expression for item1 in iterable1 if condition1
##for item2 in iterable2 if condition2
##...
##for itemN in iterableN if conditionN
##]
##
###类似于
##res=[]
##for item1 in iterable1:
##    if condition1:
##        for item2 in iterable2:
##            if condition2
##                ...
##                for itemN in iterableN:
##                    if conditionN:
##                        res.append(expression)
##

## sample 05
egg_list=[]
for i in range(10):
    egg_list.append('鸡蛋%s' %i)

print(egg_list)

##用列表生成式可以一行解决
egg_list=['鸭蛋%s' %i for i in range(10)]
print(egg_list)


##3.3 生成器表达式
##创建一个生成器对象有两种方式，一种是调用带yield关键字的函数
##另一种就是生成器表达式，与列表生成式的语法格式相同，
##只需要将[]换成()，即可：
##（expression for item in iterable if condition）

##对比列表生成式返回的是一个列表，生成器表达式返回的是一个生成器对象
#sample 06
g1=(x*x for x in range(3))
print(g1)
print(next(g1))
print(next(g1))
print(next(g1))
##print(next(g1))


## sample 07
##读取一个大文件的字节数，应该基于生成器表达式的方式完成
with open('/users/bobo/TESTBOBO','rb') as f:
    nums=(len(line) for line in f)
    total_size=sum(nums) # 依次执行next(nums)，然后累加到一起得到结果
    print(total_size)


##改造成计算文件字节数大小的函数(使用修饰器加入展示结果功能）
def showfileSize(func):
    def wrapper(*args,**kwargs):
        res= func(*args,**kwargs)
        print('file %s size is %s bit:' %(args[0],res))
        return res
    return wrapper

@showfileSize
def getfilesize(path):
    with open(path, 'rb') as f:
        nums = (len(line) for line in f)
        return sum(nums)  #依次执行next(nums),然后累加到一起得到结果

showfileSize(getfilesize('/users/bobo/TESTBOBO'))

##filesize = getfilesize('/users/bobo/TESTBOBO')
##print(filesize)



