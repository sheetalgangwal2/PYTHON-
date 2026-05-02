#Lists in Python                     #mutable -> changeable
marks = [94.4 , 76.4 , 98.3, 78.2]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(len(marks))

student = ["sheetal" ,97 , "Indore" , 19]
print(student[0])
student[0] = "neha"
print(student)

#List Slicing
marks = [24, 54 , 65 ,34 , 67]
print(marks[0:3])
print(marks[1:2])
print(marks[:3])            #[0:3]
print(marks[2:])            #[2:len(list)]
print(marks[-3:-1])         #negative slicing


#List Methods
list = [2 ,1 ,3]

list.append(4)
print(list)                   #adds one element at the end

list.sort()
print(list)                   #sorts in ascending order

list.sort(reverse=True)
print(list)                   #sorts in descending order


list = ["banana" , "apple" , "kiwi"]

list.reverse()
print(list)

list.insert(2 , "pienapple")            #insert element at index
print(list)                  

list = [2 , 1, 5 ,2 , 4, 2]
list.remove(2)
print(list)                 #removes first occurence of element

list.pop(0)
print(list)                #removes element at index


#Tuples in python                         #immutable
tup = (43 , 54, 26 , 96 ,29 , 92)
print(type(tup))
print(tup[0])
print(tup[4])
print(tup[3:5])
print(tup[0:3])

tup = ()
print(tup)

tup = (3,)               #without comma it is integer type
print(tup) 


#Tuple Method
tup = (2,1,3,1)
#tup.undex(el)
print(tup.index(2))             # returns index of first occurence

print(tup.count(1))             #counts total occurences


#WAP to ask the user to enter names of their 3 fav movies & store them in a list
movie = []

movie.append(input("enter 1st fav movie: "))
movie.append(input("enter 2nd fav movie: "))
movie.append(input("enter 3rd fav movie: "))

print(movie)


#WAP to check if a list contains a palindrome of elements.
list1 = [1, 2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")


#WAP to count the occurence of student with the grade "A" in following tuple
tuple = ["C", "D", "A" , "A", "B", "B", "A"]
print(tuple.count("A"))


#store the above values in a list & sort them from "A" to "D".
tuple = ["C", "D", "A" , "A", "B", "B", "A"]
tuple.sort()
print(tuple)