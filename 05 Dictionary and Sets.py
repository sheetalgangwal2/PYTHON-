#Dictionary in python
dict = {
    "key" : "value" ,
    "name" : "sheetal" ,
    "language" : "python",
    "age" : 19,
    "is_adult" : True,
    "marks" : 98.76,
    "subjects" : ["phy", "chem", "math"]
}
print(dict)
print(dict["name"])
print(dict["subjects"])

dict["name"] = "neha"
print(dict)
dict["surname"] = "gangwal"
print(dict)


null_dict = {}
print(null_dict)


#Nested Dictionary
student = {
    "name" : "sheetal",
    "marks" : {
        "phys" : 98,
        "chem" : 96,
        "math" : 95
    }
}
print(student)


#Dictionary Methods
student = {
    "name" : "sheetal",
    "marks" : {
        "phys" : 98,
        "chem" : 96,
        "math" : 95
    }
}
print(student.keys())           #name , marks
print(len(student))             #2
print(student.values())         #values without key
print(student.items())          #pairs of keys and values in paranthesis
print(student.get("name"))      #value of key

student.update({"name" : "kaashvi" ,"city" : "Indore", "age" : "34"})
print(student)



#Sets in python               mutable, unorederd
collection = {1, 2, 3, 4, 3, 2}
print(type(collection))          #set
print(collection)
print(len(collection))          #duplicate items ignored


variable = set()               #empty set
print(type(variable))


#Set Methods                    set -> elements -> immutable
collection = set()

collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("sheetal")

collection.remove(1)

print(collection)        #{2, 3 ,4, 'sheetal'}

print(collection.pop())   #pick random item

collection.clear()
print(len(collection))       #0


set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

print(set1.union(set2))        #{1, 2, 3, 4, 5, 6, 7}

print(set1.intersection(set2))  #{4}


#store following word meanings in python dictionary
dict = {
    "table" : {
        "a piece of furniture", 
        "list of facts & figures"
    },
    "cat" : "a small animal"
}

print(dict)


#assume one classsrom needed for 1 subject. how many claassroms are needed for all students.
subjects = {"python", "java" ,"C++", "python" ,"javascript", "java", "python", "java" ,"C++", "C"}
print("number of classroom needed : ", len(subjects))            #5


#WAP to enter marks of 3 student from the user and store them in a dictionary. start with an empty dictioanry & add one by one.
marks = {}
phys = int(input("enter physics marks : "))
chem = int(input("enter chemistry marks : "))
math = int(input("enter mathematics marks : "))

marks.update({"physics" : phys , "chemistry" : chem , "mathematics" : math})
print(marks)

#figure out a way to store 9 & 9.0 as seperated values in the set.
set = {9 , "9.0"}
print(set)