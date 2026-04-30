print("hello world!")
print("sheetal gangwal")


name = "sheetal"                     #string
age = 19                             #int
marks = 95.23                        #float
print("Welcome!", name) 
print("Your age is : ", age)
print("You scored :", marks)

age = 23
old = False
a = None
print(type(old))         #Bool
print(type(a))           #None 


#Arithematic Operators
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("sum : " , a + b)
print("difference : ", a - b)
print("product : ", a * b)
print("division : ", a / b)
print("remainder :", a % b)
print("a^b :",a ** b)            #power operator   


#Relational / Comparison Operators
p = 50
q = 20

print(p == q)       #False
print(p != q)       #True
print(p >= q)       #True
print(p <= q)       #Flase


#Assignment Operator
num = 10
num += 10     #num -=10    num *= 10         num /=10     num %=10     num **= 10 
print("num:", num)


#Logiacal Operators
print(not False)
print(not(True))

c = 20
d = 10
print(c > d)
print(c < d)


#WAP to input 2 numbers & print theirsum
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number :"))
print("Sum of both numbers :" , num1 + num2)


#WAP to input side of a sqaure & print it area.
s = int(input("enter the side of sqaure:"))
print("area of sqaure: ", s *s)


#WAP to input 2 floating point numbers & print their average.
u = float(input("Enetr first number : "))
v = float(input("Enter second number :"))
print("average of both numbers :", (u + v)/2 )

#WAP to input two integers , a and b.    print True if a is greater than or eqaul to b . tf not print False
a = int(input("enter number a:"))
b = int(input("enter number b:"))
print(a >= b)