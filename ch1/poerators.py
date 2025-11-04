# Arithmetic Operators
print("sum =", 4 + 3)
print("difference =", 4 - 3)
print("product =", 4 * 3)
print("quotient =", 4 / 3)
print("floor division =", 4 // 3)
print("modulus =", 4 % 3)
print("exponentiation =", 4 ** 3)


# Assignment Operators
x = 5
print("Initial x =", x)
x += 2
print("After x += 2 :", x)
x *= 3      
print("After x *= 3 :", x)
x -= 4      
print("After x -= 4 :", x)
x /= 2      
print("After x /= 2 :", x)
x %= 3      
print("After x %= 3 :", x)  
x **= 2     
print("After x **= 2 :", x)
x //= 2     
print("After x //= 2 :", x) 

# Comparison Operators
a = 10
b = 20
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)        
print("a >= b :", a >= b)
print("a <= b :", a <= b)


# Logical Operators
p = True
q = False
print("p and q :", p and q)
print("p or q  :", p or q)
print("not p   :", not p)
print("not q   :", not q)   


#Identity Operators
x = 5
y = 5     
print("x is y     :", x is y)
print("x is not y :", x is not y)   


# Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana in fruits :", "banana" in fruits)
print("grape in fruits  :", "grape" in fruits)
print("banana not in fruits :", "banana" not in fruits)
print("grape not in fruits  :", "grape" not in fruits)  


# Bitwise Operators
m = 5  # 0101 in binary
n = 3  # 0011 in binary         
print("m & n  :", m & n)   # AND
print("m | n  :", m | n)   # OR
print("m ^ n  :", m ^ n)   # XOR
print("~m     :", ~m)      # NOT
print("m << 1 :", m << 1)  # Left Shift
print("m >> 1 :", m >> 1)  # Right Shift