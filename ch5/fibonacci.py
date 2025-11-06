def fibonacci(n):
    if n <= 0:    # base case
        return 0
    elif n == 2:    # base case
        return 1
    else : # recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    
n = int(input("Enter a positive integer: "))
for i in range(1, n + 1):
    print(f"The {n}th Fibonacci number is {fibonacci(i)}")   
 