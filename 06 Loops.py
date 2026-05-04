#Loops 
#While loops

count = 1                      #iterator
while count <= 5:
    print("hello world")
    count += 1

print(count)           #6


i = 1
while i <= 8:
    print("sheetal", i)
    i += 1

#print numbers drom 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1

#print numbers form 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1

#print numbers form 0 to 50.
i = 0
while i <= 50:
    print(i)
    i += 1

#print the multiplication table of n.
n = int(input("Enter number : "))
i = 1
while i <= 10:
    print(i * n)
    i += 1
print("table end")


#Print the element of the following lists using a loop.
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


heroes = ["spiderman", "captain marvel","hulk", "thor", "ironman", "blackwidow", ]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1


#Search for a number x in this tuple using loop.
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("enter number:"))
i = 0
while i < len(nums):
    if(x == nums[i]):
        print("found at index" , i)
        break
    else:
        print("finding....")
    i += 1


#Break and Continue
i = 0
while i <= 5:
    print(i)
    if( i == 3):
        break
    i +=1

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

#just print odd numbrs:
i = 0
while i <= 10:
    if(i%2 ==0):
        i += 1
        continue
    print(i)
    i += 1


#print even numbers:
i = 0
while i <= 11:
        if(i%2 != 0):
             i +=1
             continue
        print(i)
        i += 1


#For loops          sequential traversal
list = [1, 2, 3, 4, 5]

for val in list:
    print(val)
   

veggies = ("potaot", "cucumber", "brinjal", "ladyfinger", "spinach")

for el in veggies:
    print(el)

str = "sheetal gangwal"
for ch in str:
    if(ch == "g"):
        print("g found ")
        break
    print(ch)



#using FOR
#Print the element of the following lists using a loop.
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in list :
    print(el)


#Search for a number x in this tuple using loop.
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 81)

x = int(input("enter number : "))
idx =0
for el in nums:
    if(x == el):
        print("number found at idx", idx)
    idx += 1


#Range
#range(start?, stop, step?)
seq = range(5)

for el in seq:
    print(el)


for i in range(11):              #range(stop)
    print(i)


for i in range(2, 11):           #range(start, stop)
    print(i)


for i in range(2 ,21, 2):         #range(start, stop , step)
    print(i)

#print even numbers from 1 to 100.
for i in range(2, 101, 2):
    print(i)

#print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)


#print the multiplication table for number n.
n = int(input("Enter number : "))

for i in range(1, 11):
    print(i * n)


#Pass Statement
for i in range(5):
    pass
print("hello world")



#WAP to find the sum of first n numbers. using while
n = int(input("enter number : "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
    print("sum of numbers : ", sum)


#WAPto find the factorial of first n numbers. using for.
n = 6
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial = ", fact)