n = int(input("Enter a number: "))

#writing a function to calculate sum of from 1 to n
def sum_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


output = sum_natural_numbers(n)
print(f"The sum of natural numbers from 1 to {n} is: {output}")# Function Examples ̰