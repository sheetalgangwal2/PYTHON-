#Conditional Statements

light = input("colour of light : ")

if(light == "green"):
    print("GO")
elif(light == "yellow"):
    print("WAIT")
elif(light == "red"):
    print("STOP")
else:
    print("light broken")



age = int(input("enter age : "))

if(age >= 18):
    print("you can drive")
elif(age < 18):
    print("you can not drive")



marks = int(input("Enter marks :"))
if(marks >= 90):
    print("A")
elif(90 > marks >= 80 ):
    print("B")
elif(80 > marks >= 70):
    print("C")
elif(70 > marks):
    print("D")


#Nesting
age = int(input("enter age : "))

if(age >= 18):
    if(age >= 80):
        print("can not drive")
    else:
     print("can drive")
else:
    print("can not drive")


#WAP to check if a number enterd by user is odd or even.
num = int(input("enter number : "))
if(num %2 == 0 ):
    print("EVEN")
else:
    print("ODD")


#WAP to find the greatest of 3 numbers enterd by the user:
a = int(input("enter number a : "))
b = int(input("enter number b : "))
c = int(input("enter number c : "))

if(a >= b and a >= c):
    print("a is greatest number" , a)
elif(b >= a and b >= c):
    print("b is greatest number" ,b)
elif(c >= a and c >= b):
    print("c is greatest number", c)


#WAP to check if a number is multiple of 7 or not
num = int(input("enter number : "))
if(num%7 == 0):
    print("number is multiple of 7")
else:
    print("number is not a multiple of 7")