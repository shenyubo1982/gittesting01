##07-05 学习笔记
##装饰器
##——————————————————————————————————
## 2.1 无参数装饰器的实现
##如果想为下述函数添加统计其执行时间的功能
import time


def index():
    time.sleep(3)
    print('1.Welcome to the index page')
    return 200


index() #函数原本的执行方式

##遵循不修改被装饰器对象源代码的原则，我们想到的解决方案可能是这样↓
start_time = time.time()
index()
stop_time = time.time()
print('1.run time is %s' % (stop_time - start_time))


##考虑到还有可能要统计其他函数的执行时间，于是我们将其作成一个单独的工具
##函数体需要外部传入被装饰的函数从而进行调用，我们可以使用参数的形式传入

def warapper(func):
    start_time = time.time()
    res = func()
    stop_time = time.time()
    print('2.run time is %s' % (stop_time - start_time))
    return res

##但之后函数的调用方式都需要统一改成
warapper(index) #函数执行【与原本的执行方式放生了变化】

##↑：由于调用方式都需要调整成warapper(index),不是原来的index()了。
## 这样的操作，违反了不能修改被装饰对象调用方式的原则，
##于是我们换一种为函数体传值的方式，即将值【包给函数】，如下↓
def timer(func):
    def wrapper():
        start_time = time.time()
        res = func()
        stop_time = time.time()
        print('3.run time is %s' % (stop_time - start_time))
        return res
    return wrapper


##这样我们便可以在不修改被装饰函数源代码和调用方式的前提下为其加入统计时间的功能，
##只不过需要事先执行一次timer被装饰的函数传入，返回一个闭包函数wrapper
##重新赋值给变量名/函数名index，如下
index = timer(index) #装饰：将被装饰的函数进行装饰
## （↑因为装饰器 timer(index)返回的是函数对象wrapper，这条语句相当于index=wrapper
index() ##函数执行【没有改变函数的执行方式】，
## （此时，执行了index()就相当于执行wrapper()
##timer就是一个装饰器，他一个普通的函数，它把执行真正业务逻辑的函数func包裹在其中个，
##看起来像index被timer装饰了一样，timer返回的也是一个函数，这个函数的名字叫wrapper。
##在这个例子中，函数进入和退出时，被称为一个横切面，这种编程方式称为面向切面的编程。


##至此，我们便实现了一个无参装饰器timer，可以在不修改被装饰对象index源代码和
##调用方式的前提下为其加上新功能。但我们忽略了若被装饰的函数是一个有参函数，
##便会抛出异常
##引出带参数的装饰器


##如果按照如下操作会报错
def home(name):
    time.sleep(5)
    print('2.welecom to the home page',name)

#home=timer(home)
#home('egon')

##抛异常的原因是，home('egon')调用的其实是wrapper('egon'),而函数wrapper没有参数
##wrapper函数接收的参数其实是给最原始func用的，为了能满足被装饰函数参数的所有情况，
##使用*args+**kwargs组合（见4.3小节），于是修正装饰器timer2如下
def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time= time.time()
        print('4.run time is %s' %(stop_time-start_time))
        return res
    return wrapper
##此时我们就可以用timer2来装饰带参数或不带参数的函数了，但是为了简洁而优雅地使用装饰器
##python提供了专门的装饰器语法来取代 index=timer2(index)的形式，需要在被装饰对象的正上方
##单独一行添加@timer2，当解释器解释到@timer2时，就会调用timer2函数，并且把它正下方
##的函数名当做实参传入，然后将返回的结果重新赋值给原函数名
@timer # index = timer(index)
def index():
    time.sleep(3)
    print('3.Welcom to the index page')
    return 200
@timer # index = timer(index) 如果有多个修饰器可以叠加多个
def home(name):
    time.sleep(5)
    print('4.Welcom to the home page',name)

#index()
#home()

##2.2 有参数的装饰器的实现
##了解无参数装饰器的实现原理后，我们可以再实现一个用来为被装饰对象添加认证功能的装饰器，
##实现的基本形式如下：

def deco(func):
    def wrapper(*args,**kwargs):
        #编写基于文件的认证，认证通过则执行res=func(*args，**kwargs)
        #并返回res
        return True
    return wrapper


##如果我们想提供多种不同的认证方式以供选择，单从wrapper函数的实现角度改写如下：
def deco(func):
    def wrapper(*args,**kwargs):
        if driver == 'file':
            # 编写基于文件的认证，认证通过则执行res=func(*args，**kwargs)
            # 并返回res
            return True
        elif driver =='mysql':
            # 编写基于文件的认证，认证通过则执行res=func(*args，**kwargs)
            # 并返回res
            return True
    return wrapper
##以上wrapper函数需要一个参数driver，而函数deco与wrapper的参数都有其特定的功能，
##不能用来接收其他类别的参数，可以从deco的外部再包一层函数auth，用来专门接收额外的参数，
##这样变保证了auth函数内无论多少层都可以引用到
def auth(driver):
    def deco(func):
        def wrapper(*args, **kwargs):
            if driver == 'file':
            # 编写基于文件的认证，认证通过则执行res=func(*args，**kwargs)
            # 并返回res
                print('dirver=file')
                return True
            elif driver == 'mysql':
                print('driver=mysql')
                return True
        # 编写基于文件的认证，认证通过则执行res=func(*args，**kwargs)
        # 并返回res
        return wrapper
    return deco
##此时，我们就实现了一个带参数的装饰器，使用方法如下：
##先调用auth_type(driver=file),得到@deco，deco是一个闭包函数
##包含了对外部作用域名字driver的引用，
##@deco的语法意义与无参数装饰器一样
@auth(driver='file')
def index():
    pass

@auth(driver='mysql')
def home():
    pass

index=deco(index)
home=deco(home)


##-------new  example


