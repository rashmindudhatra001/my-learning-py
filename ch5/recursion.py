def factorial (n):
    
    
    #base case
    if n == 0:
        return 1
    
    #recursive case
    ans = n * factorial(n-1)
    return ans

n = input("Enter a non-negative integer: ")   


print (f"The factorial of {n} is {factorial(n)}")