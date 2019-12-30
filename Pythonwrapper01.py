## example 01 简单的装饰器
def use_logging(func):
    def wrapper():
        print("01. %s is running" % func.__name__)
        return func()  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()

    return wrapper


def foo():
    print('i am foo')


foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()  # 执行foo()就相当于执行 wrapper()


## example 02 使用@语法糖
def use_logging(func):
    def wrapper():
        print("02. %s is running" % func.__name__)
        return func()  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()

    return wrapper


@use_logging
def foo():
    print('i am foo')


foo()  # 执行foo()就相当于执行 wrapper()


##example 03 修饰器传递单个参数
def use_logging(func):
    def wrapper(name):
        print("03. %s is running " % func.__name__)
        return func(name)

    return wrapper


@use_logging
def foo(name):
    print('i am %s' % name)


foo('foo-Name03')


## example 04  装饰器传递多个参数
def use_logging(func):
    def wrapper(*args):
        print("04. %s is running " % func.__name__)
        return func(*args)

    return wrapper


@use_logging
def foo(name, arg, height):
    print("I am %s, age %s, height %s" % (name, arg, height))


foo("BOBO", 18, 182)
foo("BOBO", 18, 201)


## example 05 装饰器传递多个参数，同时还有多个关键字参数
def use_logging(func):
    def wrapper(*args, **kwargs):
        print("05. %s is running " % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@use_logging
def foo(name, age=None, height=999):
    print("I am %s,age %s ,height %s" % (name, age, height))


foo('Jadon')


# example 06 带参数的的装饰器
def use_logging(level):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if level == "warn":
                print("%s is running (warn) " % func.__name__)
            elif level == "info":
                print("%s is running (info) " % func.__name__)
            return func(*args,**kwargs)
        return wrapper
    return decorator

@use_logging(level="info")
def foo(name='foo06'):
    print("i am %s " % name)

foo()

## example 07 functools.wraps

def logged(func):
    def with_logging(*args,**kwargs):
        print("func.__name__ is %s " % func.__name__)
        print("func.__doc__ is %s " % func.__doc__)
        return func(*args,**kwargs)
    return with_logging

@logged
def f(x,y=1):
    """does some math!"""
    print("it's f(x)")

f(1,2)
##logged(f)




