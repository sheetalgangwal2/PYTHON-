#Object-Oriented Programming
#to make with real world scenario

#Class & Object in python 

#Class is blueprint for creating objects.

class Student:                          #creating class
    name = "Sheetal Gangwal"

s1 = Student()                            #creating object(instance)
print(s1)
print(s1.name)

s2 = Student()
print(s2.name)



class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1)
print(car1.color)
print(car1.brand)

car2 = Car()
print(car2.color)

car3 = Car()
print(car3.brand)


#__init__ function

#Constructor
class Student:
    college_name = "ABC college"
    name = "anonymous"       #class attr
    
    def __init__(self, name, marks ):
        self.name = name         #obj attr
        self.marks = marks
        print("adding new student in database")


    def welcome(self):
        print("welcome! student", self.name)

s1 = Student("vihaan", 97)
s1.welcome()

print(s1.name, s1.marks)


print(Student.college_name)

print(s1.name)     #obj attr > class attr


#create a student class that takes name & marks of 3 subjects oas argument in constructor.
#then create a method to print the avg.

class Student:

    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
       sum = 0
       for val in self.marks:
           sum += val
       print("hello",self.name, "your avg score is ", sum/3 )

s1 = Student("vihaan", [95, 94, 87])

s1.get_avg()