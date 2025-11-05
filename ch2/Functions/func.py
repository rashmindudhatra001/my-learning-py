#write a functin that print a hello world
def hello_world():
    print("Hello, World!")  
hello_world()



#add number function
def add_numbers(a, b):
    sum = a + b
    return sum


#positional arguments
print("The sum is:", add_numbers(5, 10))



#keyword arguments
print("The sum is:", add_numbers(b=15, a=25))


#aebitrary arguments
def addAllNumbers(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

output = addAllNumbers(1, 2, 3, 4, 5)
print("The sum of all numbers is:", output) 


#

#arbitrary keyword arguments
def studentinfo(**kwargs):
    for x, y in kwargs.items():
        print(f"{x}: {y}")
        
studentinfo(name="John", age=22, course="Computer Science")
studentinfo(name="Alice", age=24, course="Mathematics")     