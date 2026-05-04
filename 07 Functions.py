#Functions in python
#blocks of statements that perform a specific task.

def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(3, 5)         #function call
calc_sum(5, 6)

#we use function to reduce redundancy.

def calc_sum(a, b):
    return a + b

sum = calc_sum(1, 2)
print(sum)


def print_hello():
    print("hello")

print_hello()

#average of three numbers.
def calc_avg(a, b , c):
    sum = a + b + c
    avg = sum/3
    print(avg)

calc_avg(4, 2, 6)


#Default parameters               #when no argument is passed
def calc_prod(a=4, b=3):
    prod = a * b
    print(prod)

calc_prod()


#WAP to print the length of a list.
list = [1, 4, 6, 3, 65, 34, 2]
cities = ["pune", "noida", "delhi", "punjab"]

def print_len(list):
    print(len(list))

print_len(list)
print_len(cities)


#WAF to print the elements of a list in a singl line.
list = [1, 4, 6, 3, 65, 34, 2]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(list)


#WAF to find the factorial of n.

def calc_fact(n):
    fact = 1
    for i in range (1, n+1):
       fact *= i
    print(fact)
    
calc_fact(6)

#WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD=", inr_val, "INR" )

converter(100)