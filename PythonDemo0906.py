## 09-06 反射、内置方法

#一、反射
## 在Python中，反射指的是通过字符串来操作对象的属性，
## 涉及到四个内置函数的使用（python中类和对象都可以用下述四个方法）

# sample 01
class Teacher:
    def __init__(self,full_name):
        self.full_name = full_name

    def talk(self):
        print("i can talking 'hello!' ")


t = Teacher('Egon Lin')

#按字符串'full_name'判断有误属性t.full_name
#hasattr(object,'name')
print("hasattr(object,'name')")
print(hasattr(t,'full_name'))
print(hasattr(t,'full_names'))

#等同于t.full_name,不存在该属性则返回默认值None
#getattr(object,'name',default=None)
print("getattr(object,'name',default=None)")
print(getattr(t,'full_name',None))
print(getattr(t,'full_names',None))

print("find talk function.....")
functalk = getattr(t,'talk',None)
functalk()


#setattr(x,'y',v)
print("setattr(x,'y',v)")
setattr(t,'age',18) #等同于t.age=18
print("t.age:" , t.age)

#delattr(x,'y')
print("delattr(x,'y')")
delattr(t,'age') # 等同于del t.age
#print("t.age:",t.age) 会报错，因为age已经被删除了。


##基于反射可以十分灵活地操作对象的属性，比如将用户交互的结果反射到具体的功能执行
class FtpServer:
    def server_forever(self):
        res = True
        while res:
            inp = input('input your cmd>>:').strip()
            cmd,file = inp.split()
            if hasattr(self,cmd): ##根据用户输入的cmd，判断对象self有无对应的方法属性
                func=getattr(self,cmd) #根据字符串cmd，获取对象self对应的方法属性
                res = func(file)

    def get(self,file):
        print('Downloading %s...' %file)
        return True

    def put(self,file):
        print('Uploading %s...' %file)
        return True

    def exit(self,file):
        return False

server = FtpServer()
server.server_forever()



##二、内置方法
## python的Class机制内置了很多特殊的方法来帮助使用者高度定制自己的类，
## 这些内置方法都是以双下划线开头和结尾的，会在满足某种条件时，自动触发，
## 我们常用的__str__ 和 __del__ 为例子简单介绍

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self): ##__str__ 方法会在对象被打印时自动触发
        return '<Name:%s Age:%s>' %(self.name,self.age)

    def __del__(self):
        ## __del__ 会在对象呗删除时自动触发。由于python自带的垃圾回收机制会自动清理
        ## python程序的资源，所以当一个对象只占用应用程序资源时，完没有必要为对象定制
        ## __del__方法，但在产生一个对象的同时，涉及到申请系统资源（比如打开系统文件、
        ## 网络连接等）情况下，关于系统资源的回收，python的垃圾回收机制无法起作用，
        ## 需要我们为对象定制该方法，用来在对象被删除时自动触发回收系统资源的操作，
        ## 比如 self.conn.close() 关闭网络连接、回收系统资源。
        print("Cat is deleted")


cat = Cat('jacky',7)
print(cat) # 触发cat.__str__()，拿到返回值后进行打印


