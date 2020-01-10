# 异常处理
## python PermissionError学习
## python TypeError学习
## https://www.runoob.com/python/python-exceptions.html


## raise 引发一个异常，异常对象必须有一个名字，并且他们应该
## 是Error或者Exception类的子类
def mytest(par):
    if par == 1:
        raise Mybaseexception("自定义的异常错误信息")


class Mybaseexception(BaseException):
    def showerrormsg(self):
        print('showerrormsg:',self.__dict__)

# SAMPLE 01
mytest(1)
