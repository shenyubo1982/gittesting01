## 09-03 继承与派生

##继承：是一种创建新类的方式，
# 在python中，新建的类可以继承一个或多个父类，
# 新建的类可称为子类或派生类，
# 父类又可称为基类或超类

# sample 01
class ParentClass1: # 定义父类
    pass

class ParentClass2: #定义父类
    pass

class SubClass1(ParentClass1): #单继承
    pass

class SubClass2(ParentClass1,ParentClass2): #多继承
    pass

##通过类的内置属性 __bases__可以查看类继承的所有父类
print("查看SubClass2的所有父类")
print(SubClass2.__bases__)

## 在python3中，即使没有显示地继承object，也会默认继承该类
print("查看ParentClass1 和2 的父类")
print(ParentClass1.__bases__)
print(ParentClass2.__bases__)
## 因而在python3中统一都是新式类，关于经典类与新式类的区别，后面讨论
## 提示：object类提供了一些常用内置方法的实现，如用来在打印对象时返回字符串的内置方法__str__



# 二、继承与抽象
## sample 02
class People:
    school = '清华大学'

    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age =age


class Student(People):
    def choose(self):
        print('%s is choosing a course' %self.name)


class Teacher(People):
    def teach(self):
        print('%s is teaching' %self.name)

#teacher类内并没有定义__init__方法，但是会从父类中找到__init__,因而仍然可以正常实例化
print("继承实验....")
teacher1 = Teacher('lili','male',18)
print(teacher1.name,teacher1.sex,teacher1.age)


## 三、属性查找
## 有了继承关系，对象在查找属性时，先从对象自己的__dict__中找，如果没有则去子类中找，
## 然后再去父类中找
## sample03

class Foo:
    def f1(self):
        print("Foo.f1")

    def f2(self):
        print('Foo.f2')
        self.f1()

class Bar(Foo):
    def f1(self):  ##这种情况下，子类Bar的f1覆盖了父类Foo的f1
        print('Bar.f1')

print('sample 03 start...')
b =Bar()
b.f2()
# 步骤解析 b.f2()会在父类Foo中找f2，先打印Foo.f2，然后执行self.f1(),即b.f1()
## 仍会按照： 对象本身->类Bar->父类Foo的顺序依次找下去，在类Bar中找到f1，因而打出Foo.f1

##父类如果不想让子类覆盖自己的方法，可以采用双下划线开头的方式将方法设置为私有的
#sample 04
class Foo2:
    def __func1(self):   ##变形为 _FOO2__func1
        print('Foo2.func1')

    def func2(self):
        print('Foo2.func2')
        self.__func1()   ##变形为 self._FOO__func1

class Bar2(Foo2):
    def __func1(self):  #变形为 _Bar2__func1
        print('Bar2.func1')

print('sample 04...')
b2 = Bar2()
b2.func2()


#四、继承的实现原理
## 对于你定义的每一个类，python都会计算出一个方法解析顺序（MRO）列表，
# 该MRO列表就是一个简单的所有基类的线性顺序列表，如下
print("Subclass2的MRO列表：")
print(SubClass2.mro()) ## 新式类内置了mro方法可以查看线性列表的内容，经典类没有该内置方法
##MRO列表的构造是通过一个C3线性化算法那来实现的，我们无需深究该算法那的数学原理，
# 它实际上就是合并所有父类的MRO列表，且在查找属性时，python会基于MRO列表按照从左到右
# 的顺序依次查找基类，直到找到第一个匹配这个属性的类为止

##当类是经典类时，多继承情况下，在要查找属性不存在时，会按照深度优先的方式查找下去
##当类是新式类时，多继承情况下，在要查找属性不存在时，会按照广度优先的方式查找下去


## 五、派生与方法重用
# 子类可以派生出自己新的属性，在进行属性查找时，子类中的属性名会优先于父类被查找，
##例如每个老师还有职称这一属性，我们就需要在Teacher类中定义该类自己的__init__覆盖父类的。
## sample05

class People2:
    school = '清华大学'

    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age =age


class Teacher2(People):
    def __init__(self,name,sex,age,title): #派生
        ## 此处有重复代码↓
        ##self.name = name
        ##self.sex = sex
        ##self.age = age
        ## 此处有重复代码↑

        ## 改良方案1 指定某个类的函数
        ##People2.__init__(self,name,sex,age)
        ##self.title = title

        ## 改良方案2
        ## 调用super()会得到一个特殊的对象，该对象专门用来引用父类的属性，
        ## 并且严格按照MRO规定的顺序向后查找
        ## 关于在子类中重用父类功能的方式，推荐使用super()
        super().__init__(name,sex,age) ##python3的书写方式
        ##super(Teacher2, self).__init__(name,sex,age) ##python2的书写方式
        self.title = title

    def teach(self):
        print('%s is teaching!' %self.name)

print("Sample 05 ....")
objt2 = Teacher2('SHENYUBO','FEMALE',38,'高级讲师')
print(objt2.name,objt2.age,objt2.sex)
print("讲师职称：", objt2.title)
objt2.teach()



## 六、组合
## 在一个类中以另外一个类的对象作为数据属性，称为类的组合。
## 组合与继承都是用来解决代码的重用性问题。
## 不同的是：继承是一种"是"的关系 ； 组合是"有"的关系。
# 当类之间有显著不同，并且较小的类是较大的类所需要的组件时，应该使用组合。

##sample 06

class Course6:
    def __init__(self,name,period,price):
        self.name = name
        self.period=period
        self.price = price
    def tell_info(self):
        print('<%s %s %s>' %(self.name,self.period,self.price))


class Date:
    def __init__(self,year,mon,day):
        self.year =year
        self.mon = mon
        self.day =day

    def tell_birth(self):
        print('<%s %s %s>' %(self.year, self.mon,self.day))


class People6:
    school = '北 京 大 学'
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age


class Teacher6(People6):
    def __init__(self,name,sex,age,title,year,mon,day):
        super().__init__(name,sex,age)
        self.birth=Date(year,mon,day)
        self.courses=[]

    def tech(self):
        print("%s is Teaching" %self.name)


print("sample 06 start....")
python = Course6('phthon','3mons',3000.0)
linux = Course6('Linux','5mons',5000.0)
teacher6 = Teacher6('杨老师','male',44,'博士',1990,3,23)

teacher6.courses.append(python)
teacher6.courses.append(linux)
teacher6.birth.tell_birth()

for obj in teacher6.courses:
    obj.tell_info()





