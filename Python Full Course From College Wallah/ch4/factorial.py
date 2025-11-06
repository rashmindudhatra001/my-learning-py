#fucation for factorial of a number
def factorial(n):  
    ans = 1     
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            ans *= i
    return ans


n = int(input("Enter a number to find its factorial: "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")