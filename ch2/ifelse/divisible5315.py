#
num = int(input("Enter a number: "))

# Checking if the number is divisible by 5 and 3
if num % 15 == 0:
    print("The number is divisible by 15 ")
else:
    if num % 5 == 0 and num % 3 == 0:   
        print("The number is not  divisible by 15 but divisible by 3 and 5")
    else:
        print("The number is not divisible by 3 and 5")    