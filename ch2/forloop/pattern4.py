n = int(input("Enter a number: "))

for i in range (1,n+1):#loop for rows
    for j in range (1 , i+1):#loop for columns
        print(chr(64+j) , end = "")#to avoid new line after each print
    print()#to move to next line after each row