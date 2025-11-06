def power_a_b(a, b):
    # base case
    if b == 0:
        return 1
    # recursive case
    return a * power_a_b(a, b - 1)  
a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
print(f"{a} raised to the power of {b} is {power_a_b(a, b)}")