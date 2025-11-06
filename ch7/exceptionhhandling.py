a = int(input ("Enter a: "))
b = int(input ("Enter b: "))

# initialize result so it's always defined even if input conversion fails or other exceptions occur
result = None

try:
    result = a / b
except ZeroDivisionError:
    result = None
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed." ,result)    
