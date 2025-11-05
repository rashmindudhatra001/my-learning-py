
#Taking two numbers as input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


#Taking  operator as input from user

operators = input("Enter operator (+, -, *, /): ")

# Performing calculations based on the operator using match case
match operators:
    #Addition case
    case "+":
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    # Subtraction case 
    case "-":
        print(f"The difference of {num1} and {num2} is {num1 - num2}")  
    # Multiplication case
    case "*":
        print(f"The product of {num1} and {num2} is {num1 * num2}")
    # Division case
    case "/":
            print(f"The division of {num1} and {num2} is {num1 / num2}")
    # Modulus case        
    case "%":
            print(f"The modulus of {num1} and {num2} is {num1 % num2}")
    # Floor division case 
    case "//":
            print(f"The floor division of {num1} and {num2} is {num1 // num2}")     
    # Exponentiation
    case "**":
            print(f"The exponentiation of {num1} and {num2} is {num1 ** num2}")
                                
     # Invalid operator   
    case _:
        print("Invalid operator")        
   
                                   

