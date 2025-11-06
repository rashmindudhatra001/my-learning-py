

n = int(input("Enter a number: "))

for i in range (n):#loop for rows
    print(" " * (n-i) , end = "")#to avoid new line after each print
    for j in range (1 , 2*i):#loop for columns
        print(j , end = "")#to avoid new line after each print
    print()#to move to next line after each row    