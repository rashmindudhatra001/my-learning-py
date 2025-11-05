# operators.py
# A comprehensive demonstration of various Python operators
def line():
    print("-" * 60)

# 1) Arithmetic Operators
# +, -, *, /, // (floor division), % (modulo), ** (power)
a = 10
b = 3
print("Arithmetic operators:")
print(f"a = {a}, b = {b}")
print("a + b =", a + b)        # Addition
print("a - b =", a - b)        # Subtraction
print("a * b =", a * b)        # Multiplication
print("a / b =", a / b)        # Division (float)
print("a // b =", a // b)      # Floor division
print("a % b =", a % b)        # Remainder
print("a ** b =", a ** b)      # Exponentiation
line()

# 2) Assignment Operators
# =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=
print("Assignment operators:")
x = 5
print("Initially x =", x)
x += 2    # x = x + 2
print("x += 2 ->", x)
x *= 3    # x = x * 3
print("x *= 3 ->", x)
x //= 4   # floor divide and assign
print("x //= 4 ->", x)
x %= 3
print("x %= 3 ->", x)
# Bitwise assignment
y = 8  # binary 1000
y >>= 2
print("y = 8; y >>= 2 ->", y, "(bit shift right, 1000 >> 2 = 10 (binary) = 2)")
line()

# 3) Comparison Operators
# ==, !=, >, <, >=, <=
print("Comparison operators:")
p = 7
q = 5
print("p == q ->", p == q)
print("p != q ->", p != q)
print("p > q ->", p > q)
print("p < q ->", p < q)
print("p >= q ->", p >= q)
print("p <= q ->", p <= q)
line()

# 4) Logical Operators
# and, or, not
print("Logical operators:")
print("True and False ->", True and False)
print("True or False ->", True or False)
print("not True ->", not True)
# Example with variables
age = 20
has_id = True
print("age >= 18 and has_id ->", age >= 18 and has_id)
line()

# 5) Bitwise Operators
# &, |, ^, ~, <<, >>
print("Bitwise operators:")
m = 6   # 110
n = 3   # 011
print("m =", m, "n =", n)
print("m & n ->", m & n)   # AND -> 010 (2)
print("m | n ->", m | n)   # OR  -> 111 (7)
print("m ^ n ->", m ^ n)   # XOR -> 101 (5)
print("~m ->", ~m)         # NOT -> two's complement
print("m << 1 ->", m << 1) # Left shift (110 << 1 = 1100 -> 12)
print("m >> 1 ->", m >> 1) # Right shift (110 >> 1 = 11 -> 3)
line()

# 6) Membership Operators
# in, not in
print("Membership operators:")
fruits = ["apple", "banana", "mango"]
print("'apple' in fruits ->", "apple" in fruits)
print("'grape' not in fruits ->", "grape" not in fruits)
line()

# 7) Identity Operators
# is, is not
print("Identity operators:")
a_list = [1, 2, 3]
b_list = a_list
c_list = [1, 2, 3]
print("a_list is b_list ->", a_list is b_list)     # same object
print("a_list is c_list ->", a_list is c_list)     # same content but different object
print("a_list == c_list ->", a_list == c_list)     # value equality
line()

# 8) Ternary Operator (Conditional Expression)
# syntax: <value_if_true> if <condition> else <value_if_false>
print("Ternary operator:")
num = 8
parity = "even" if num % 2 == 0 else "odd"
print(f"{num} is {parity}")
line()

# 9) Walrus Operator (:=) — Python 3.8+
# Allows assignment inside expressions
print("Walrus operator (:=) example:")
if (n_chars := len("hello")) > 3:
    print("length is", n_chars)
line()

# 10) String Operations
# Concatenation and repetition
print("String operators:")
s1 = "Hello"
s2 = "World"
print("s1 + ' ' + s2 ->", s1 + " " + s2)  # Concatenation
print("s1 * 3 ->", s1 * 3)                # Repetition
line()

# 11) Practical Example — Function using all operators
def demo_all(x, y):
    """Show arithmetic, comparison, logical, and bitwise examples together"""
    print("demo_all:", x, y)
    print("sum:", x + y)
    print("diff:", x - y)
    print("prod:", x * y)
    print("div:", x / y if y != 0 else "division by zero")
    print("floor div:", x // y if y != 0 else "div by zero")
    print("mod:", x % y if y != 0 else "div by zero")
    print("power:", x ** 2)
    print("compare == :", x == y)
    print("and:", (x > 0) and (y > 0))
    print("or:", (x > 0) or (y > 0))
    print("bitwise &:", int(x) & int(y))
    print("membership '1' in str(x):", "1" in str(x))

demo_all(9, 4)
line()

print(" Program finished — Try changing the values to see different outputs.")
