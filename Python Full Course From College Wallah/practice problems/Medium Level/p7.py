# 7. Write a program to generate the Fibonacci sequence up to n terms using recursion.


n = int(input("Enter the number of terms for Fibonacci sequence: "))

def fibonacci_recursive(term):
    
    if term <= 0:
        return 0
    elif term == 2:
        return 1
    else:
        return fibonacci_recursive(term - 1) + fibonacci_recursive(term - 2)
    
for i in range(1, n + 1):
    print(f"Fibonacci number {i}: {fibonacci_recursive(i)}")











