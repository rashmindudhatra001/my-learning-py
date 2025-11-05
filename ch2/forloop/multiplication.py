
n = int(input("Enter a number: "))

for i in range (1,11):
    print(n,end="  * ")
    print(i,end=" = ")
    for j in range (1,2):
        print(i*n,end=" ")
    print()