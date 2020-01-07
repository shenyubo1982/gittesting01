x = 1
print('__name__',__name__)

##全局变量
def get():
    print('get...')
    print(x)

def change():
    print("change...")
    global x   ##global关键字用来在函数或者其他局部作用域中，使用全局变量
    x =0

def add():
    print("add...")
    global x
    x += 1


class Foo:
    def func(self):
        print("from the func")



def makecount():
    print("makecount funciont ")
    count = 0    ## 外层变量
    def counter():
        nonlocal count ##nonlocal 关键字用来在函数或其他作用域中使用外层（非全局）变量
        count+=1
        return count
    return counter


def makecounttest():
    print("makecounttest function is running!")
    mc = makecount()
    print(mc())
    print(mc())
    print(mc())


if __name__ =='__main__': ##需要自测的逻辑，但是在希望其他程序调用的时候不执行的逻辑
    makecounttest()

