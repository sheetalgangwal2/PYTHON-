#Four pillars of object-oreiented preogramming.

#Abstraction
#hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.brk = True
        self.acc = True
        print("car started")

car1 = Car()
car1.start()

#Encapsulation
#wrapping data and functions into a single unit(object).


#Create account class with 2 attr- balance & account no.
#create method for debit , credit & printing the balance.

class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_no = acc_no
        
    def debit(self, amount):
            self.balance -= amount
            print("Rs.", amount,"was debited" )
            print("Total balance : ", self.get_balance())

    def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "was credited")
            print("Total balance : ", self.get_balance())

    def get_balance(self):
            return self.balance

acc1 = Account(10000, 1234)
acc1.debit(1000)
acc1.credit(500)


#del keyword
#used to delete object properties or object itself.

# class Student:
#       def __init__(self, name):
#             self.name = name

# s1 = Student("sheetal")
# print(s1.name)
# del s1.name
# print(s1.name)         


#private(like)
class Account:
      def __init__(self, acc_no, acc_pass):
            self.__acc_no = acc_no     #__ to keep it private
            self.__acc_pass = acc_pass

acc1 = Account("1234", "abcd")

# print(acc1.__acc_no, acc1.__acc_pass)      #error


#Inheritance
#when one class(child/derived) derives the properties & methods of another class.(parent/base)

#Single Inheritance
class Car:
      color = "black"
      @staticmethod
      def start():
            print("car started")

      @staticmethod
      def stop():
            print("car stopped")

class ToyotaCar(Car):
      def __init__(self, name):
            self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start())
print(car1.color)

#Multi-level Inheritance
class Car:
      color = "black"
      @staticmethod
      def start():
            print("car started")

      @staticmethod
      def stop():
            print("car stopped")

class ToyotaCar(Car):
      def __init__(self, brand):
            self.brand = brand

class Fortuner(ToyotaCar):
      def __init__(self, type):
            self.type = type

car1 = Fortuner("diesel")
car1.start()

#Multiple Inheritance
class A:
      varA = "welcome to class A"

class B:
      varB = "welcome to class B"

class C(A, B):
      varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)


#Super Method
#super() method is used to access methods of the parent class.

class Car:
      def __init__(self, type):
            self.type = type

      @staticmethod
      def start():
          print("car started")

      @staticmethod
      def stop():
          print("car stopped")

class ToyotaCar(Car):
      def __init__(self, name, type):
          self.name = name
          super().__init__(type)


car1 = ToyotaCar("prius", "electric")
print(car1.type)



class Person:
     name = "anonymous"

     #def changename(self, name):
          #Person.name = name
          #self.__class__.name = "sheetal"

     @classmethod
     def changename(cls, name):
          cls.name = name

p1 = Person()
p1.changename("sheetal gangwal")
print(p1.name)
print(Person.name)


#Property
#to sue the method as a property.
class Student:
     def __init__(self, phy, chem, math):
          self.phy = phy
          self.chem = chem
          self.math = math
          
     @property
     def percentage(self):
         return str((self.phy + self.chem + self.math)/3) + "%"
          

s1 = Student(98, 97, 84)
print(s1.percentage)

s1.phy = 86
print(s1.percentage)


#Polymorphism : operator overloading
#when the same operator is allowed to have different meaning according to the context.

class Complex:
      def __init__(self, real, img):
            self.real = real
            self.img = img

      def showNumber(self):
            print(self.real , "i +", self.img, "j" )

      def __add__(self, num2):           #dundur function
            newReal = self.real + num2.real
            newImg = self.img + num2.img
            return Complex(newReal, newImg)

      def __sub__(self, num2):
            newReal = self.real - num2.real
            newImg = self.img - num2.img
            return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 7)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

