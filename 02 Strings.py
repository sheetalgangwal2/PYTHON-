str1 = "Sheetal"
str2 = "Gangwal"
print(str1 + str2)           #Concatenation

str = "sheetal gangwal"
print(len(str))     #15


#Indexing
string = "sheetal"
ch = string[0]
ch1 = string[4]
print(ch)
print(ch1)


#Slicing
str = "python"
print(str[2:5])            #ending index not included
print(str[:3])             #[0:3]
print(str[1:])             #[1: len(str)]
print(str[-5:-1])          #negative slicing


#String Function
str = "i am a coder."

print(str.endswith("er."))      #true
print(str.endswith("al."))      #false

print(str.capitalize())

print(str.replace("coder" , "programmar"))           #("old" , "new")

print(str.find("a"))          #2
print(str.find("t"))

print(str.count("am"))        #1
print(str.count("z"))         #0


#WAP to input user's first name & print its lenght.
name = input("Enter your first name : ")
print(len(name))

#WAP to find the occurence of "$" in a string.
str = "currently $$$ learning # $ learning python $$$$$"
print(str.count("$"))