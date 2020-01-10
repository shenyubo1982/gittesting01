## 09-05 绑定方法与非绑定方法

## 类中定义的函数分为两大类：绑定方法和非绑定方法
## 在类中正常定义的函数默认是绑定到对象的，
## 而为某个函数加上装饰器 @classmethod后，该函数就绑定到了类。

#类方法通常用来在__init__的基础上提供额外的初始化实例的方式

#sample 01



## 二、非绑定方法（静态方法）
## 为类中某个函数加上装饰器 @staticmethod后，
## 该函数就变成了非绑定方法，也成为静态方法。
## 该方法不与类或者对象绑定，类与对象都可以来调用它，
## 但它就是一个普通函数而已，因而没有自动传值那么一说


## 总结： 绑定方法与非绑定方法的使用、
## 若类中需要一个功能，该功能的实现代码中需要应用对象，
## 则将其定义成对象方法，需要引用类则将其定义成类的方法、
## 无需引用类或对象则将其定义成静态方法。

###### 1、默认是绑定对象方法
###### 2、@classmethod 就是绑定对象方法
###### 3、@staticmethod 就是非绑定方法（静态方法）

