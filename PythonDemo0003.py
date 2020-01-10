## __base__  , __bases__ 区别
import  PythonDemo0004

from PythonDemo0004 import showlinefeed

class G(object):
    def showname(self):
        print('G')

class D(G):
    def dfunc(self):
        print('D')


class F(G):
    pass

class E(G):
    pass


class C(F):
    def cfunc(self):
        print('C')



class B(E):
    def bfunc(self):
        print('B')




class A(B,C,D):
    pass


## 实验
print("实验开始....")
print("A类的MRC列表：")
print(A.mro())

print(A.__bases__)
print(A.__base__)

##PythonDemo0004.showlinefeed(A.mro())
showlinefeed(A.mro())




