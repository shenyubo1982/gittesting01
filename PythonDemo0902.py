## 09-02 封装
## 面向对象的三大特性：封装、继承、多态。
## 封装就是把数据和功能都整合在一起。还可以严格控制对他们的访问，分两步实现：隐藏于开发接口

## 隐藏属性
## python的Class机制采用双下划线开头的方式，将属性隐藏起来（设置成私有的），
## 单这其实仅仅只是一种变形操作，类汇总所有双下划线开头的属性都会在类定义阶段、
## 检测语法时自动变成"_类名称__属性名"的形式：

## sample 01
class Foo:
    __N = 0

    def __init__(self):
        self.__x = 10


    def __f1(self):
        print('__f1 run')

    def f2(self):
        self.__f1()

## print(Foo.__N) ## 报错：类Foo没有属性__N

obj = Foo()
## print(obj.__x) ## 报错:对象obj没有属性__x

##这种变形需要注意的问题是：
## 1.在类的外部无法直接访问双下划线开头的属性，但知道了类名和属性名就可以拼出名字：
## _类名__属性，然后就可以访问了，如：Foo._A__N,所以说这种操作并没有严格意义上地限制外部访问
## 只是一种语法意义上的变形

## sample 02
print(Foo.__dict__)
print(obj.__dict__)
print("Foo._Foo__N:", Foo._Foo__N)
print("obj._Foo__N:", obj._Foo__N)

##print("Foo._Foo__x:", Foo._Foo__x)
print("obj._Foo__x:", obj._Foo__x)


## 2、在类内部，是可以直接访问双下划线开头的属性的，
## 比如 self.__f1(),因为在类定义阶段，类内部双下划线开头的属性统一发生了变形
## sample 03
obj.f2()

##Foo.f2(obj)

## 3、变形操作只在类定义阶段发生一次，在类定义之后的赋值操作，不会变形
## sample 03
Foo.__M = 100
print(Foo.__dict__) # 发现__M没有变形为_FOO__M，因为已经过了定义阶段。
print("Foo.__M: ",Foo.__M)

obj.__y = 20
print(obj.__dict__)
print("obj.__y:",obj.__y)

# 三、开放接口
## 定义属性就是为了使用，所以隐藏不是目的

## 3.1 隐藏数据属性
## 将数据隐藏起来就限制了类外部对数据的直接操作，然后类内部应该提供相应的接口
## 来允许类外部间接地操作数据，接口之上可以附加额外的逻辑来对数据操作进行严格控制
## sample 04
class Teacher:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def tell_info(self): ##对外提供访问老师信息的接口
        print('name:%s , age:%s' %(self.__name,self.__age))

    def set_info(self,name,age):
        if not isinstance(name,str):
            raise TypeError('姓名必须是字符串类型')
        if not isinstance(age,int):
            raise TypeError('年龄必须是整型')

        self.__name = name
        self.__age = age


print('实验开始......')
t = Teacher('lili',18)
t.tell_info()
print('修改老师信息....')
##t.set_info('LILI','19') ##年龄不是整型，所以会抛出异常
t.set_info('LILI',30)
t.tell_info()


## 3.2 隐藏函数属性
## 目的是为了隔离复杂度
## 例如ATM程序的取款功能，该功能有很多其他功能的组合，比如：插卡、身份验证、输入金额、打印小票等
## 而对于使用者来说，只需要开发取款这个功能接口即可，其余功能，我们可以隐藏起来。
## sample 05
class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __printbill(self):
        print('打印账单')
    def __takemony(self):
        print('取款')
    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__printbill()
        self.__takemony()

print('ATM实验开始...')
objatm = ATM()
objatm.withdraw()
##隐藏属性与开放接口，本质就是了为了明确区分内外，类内部可以修改分装内的东西而不影响外部调用者的代码，
##而类外部只需要拿到一个接口，只要接口名、参数不变，则无论设计者如何改变内部实现代码，
##使用者均无需改变代码。这就能提供一个良好的合作基础，只要接口这个基础约定不变，则代码的修改不足为虑。


## 四、property
## BMI指数是用来衡量一个人体重和身高对健康影响的一个指标
## 身高或体重是不断变化的，因而每次想查看BMI值都需要通过计算才能得到，
## 但很明显BMI听起来更像是一个特性而非功能，为此python专门提供了一个装饰器property,
## 可以将类中的函数"伪装成"对象的数据属性，对象在访问该特殊属性时会出发功能的执行，
## 然后将返回值作为本次访问的结果，例如

class People:
    __normalweight=0

    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height

    @property    #装饰器表示数据属性
    def bmi(self):
        '''
        体质指数（BMI）=体重（kg）÷身高^2（m）
        EX：70kg÷（1.75×1.75）=22.86
        :return: 计算结果
        '''
        return self.weight/(self.height**2)

    def __setbmiWeight(self):
        if self.bmi >=18.5 and self.bmi<=23.5:
            self.__normalweight=self.weight
        else :
            self.__normalweight = 23.5*(self.height*2)

    def checkMybmi(self):
        self.__setbmiWeight()
        print('【BMI标准范围是：18.5~23.5】')
        print("我标准体重极限应该是 %dKG" %self.__normalweight)


print('People 实验开始...')
objpeople = People('Bobo',90,1.83)
print("该用户的Bmi是：",objpeople.bmi)
objpeople.checkMybmi()


## 使用property有效地保证了属性访问的一致性。
## 另外property还提供设置和删除属性的功能，如下：
## sample 06
class Foo:
    def __init__(self,val):
        self.__NAME = val

    @property
    def name(self):
        return self.__NAME

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError('%s must be str' %value)
        self.__NAME = value

    @name.deleter
    def name(self):
        raise PermissionError('Can not delete')



##
print('Foo实验开始.....')
f =Foo('shenyubo')
print(f.name)
f.name="SHENYUBO"
print(f.name)
##f.name = 1
##print(f.name)
del f.name
