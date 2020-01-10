## 09-04 多态性与鸭子类型

import  abc

## 多态与多态性
## 多态指的是一类事物有多种形态，比如动物有多种形态：猫、狗、猪
#sample 01
class Animal:
    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        print("Cat talk")

class Dog(Animal):
    def talk(self):
        print("Dog talk")

class Pig(Animal):
    def talk(self):
        print("Pig talk")

cat = Cat()
dog = Dog()
pig = Pig()

cat.talk()
dog.talk()
pig.talk()

## 多态性指的是可以在不用考虑对象具体类型的情况下而直接使用对象，
## 这就需要在设计时，把对象的使用方法统一成一种：
## 例如cat、dog、pig都是动物，但凡动物肯定有talk方法，于是我们可以不用考虑
## 他们三者的具体是什么类型的动物，而直接使用talk
## 更进一步，我们可以定义一个统一的接口来使用
#sample 02
def Talk(animal):
    animal.talk()

print("定义一个统一的接口Talk来使用：")
Talk(cat)
Talk(dog)
Talk(pig)


## Python中一切皆对象，本身就支持多态性
## sample 03
s = 'abcde'
l = [1,2,3]

print(s.__len__())
print(len(s))

print(l.__len__())
print(len(l))

## 多态性的好处在于增强了程序的灵活性和可扩展性，比如通过集成Animal类创建了一个新的类
## 实例化得到的对象obj,可以使用相同的方式，使用obj.talk()

##综上所述，多态性的本质在于不同的类中定义有相同的方法名，
##这样我就可以不考虑类而统一用一种方式去使用对象，
## 可以通过在父类引入抽象类的概念来硬性限制子类必须有某些方法名


##定义抽象类之前需要import abc
## sample 04
class Animalabc(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass



class Cat2(Animalabc):
    def talk(self):
        pass

cat2 = Cat2()


## 但其实，我们完全可以不依赖继承、只需要制造出外观和行为相同对象
## 同样可以实现不考虑对象类型而使用对象
## 这正是python崇尚的"鸭子类型（duck typing)"
## "如果看起来像、叫声像而且走起路来像鸭子，那么他就是鸭子。"
## 比起继承的方式，鸭子类型在某种程度上实现了程序的送耦合度，如下：


## sample 05
## 两者看起来都像文件，因为就可以当文件一样去使用，然后他们并没有直接的关系
class Txt:  # Txt类有两个与文件类型相同的方法，即read和write
    def read(self):
        pass
    def write(self):
        pass

class Disk: # Disk类页游两个与文件类型同名的方法：read和write
    def read(self):
        pass
    def write(self):
        pass





