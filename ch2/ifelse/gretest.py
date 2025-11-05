# Taking three numbers as input from user
x = int(input("Enter a number 1 : "))     
y = int(input("Enter a number 2 : "))
z = int(input("Enter a number 3 : "))

# Comparing three numbers to find the greatest
if x > y and x > z:
    print(f"{x} is greatest number")
elif y > x and y > z:
    print(f"{y} is greatest number")
else:    
    print(f"{z} is greatest number")
    
    
    
    
 #Comparing three numbers to find the greatest using nestered if else
if x > y:
    if x > z:
        print(f"{x} is greatest number")
    else:
        print(f"{z} is greatest number")
else:
    if y > z:
        print(f"{y} is greatest number")
    else:
        print(f"{z} is greatest number")
