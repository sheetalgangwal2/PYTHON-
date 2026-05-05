#Recursion in python
#when a function calls itself repeatedly.

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)

# show(5)

n = int(input("enter number : "))
def odd_even():
    if(n%2 == 0):
        print("EVEN")
    else:
     print("ODD")

odd_even()
