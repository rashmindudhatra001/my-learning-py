# tuple_demo.py
# This program demonstrates how tuples work in Python.

def line():
    print("-" * 50)

# 1 Creating Tuples
numbers = (10, 20, 30, 40, 50)
fruits = ("apple", "banana", "mango")
mixed = (1, "hello", 3.14, True)

print("Original Tuples:")
print("numbers =", numbers)
print("fruits =", fruits)
print("mixed =", mixed)
line()

# 2 Accessing Elements (Indexing)
print("Accessing tuple elements:")
print("First fruit:", fruits[0])      # index starts from 0
print("Last fruit:", fruits[-1])      # negative index
line()

# 3 Slicing
print("Tuple Slicing:")
print("numbers[1:4] =", numbers[1:4])
print("numbers[:3] =", numbers[:3])
print("numbers[2:] =", numbers[2:])
line()

# 4 Iterating through a Tuple
print("Loop through tuple:")
for fruit in fruits:
    print(fruit)
line()

# 5 Length, Min, Max, and Sum (works only for numeric tuples)
print("Tuple Functions:")
print("Length of numbers =", len(numbers))
print("Max =", max(numbers))
print("Min =", min(numbers))
print("Sum =", sum(numbers))
line()

# 6 Tuple Methods (only two main ones)
print("Tuple Methods:")
sample = (10, 20, 10, 30, 10)
print("sample =", sample)
print("Count of 10 =", sample.count(10))   # counts occurrences
print("Index of 30 =", sample.index(30))   # finds first occurrence
line()

#7 Nested Tuples
print("Nested Tuple:")
nested = ((1, 2), (3, 4), (5, 6))
print("nested =", nested)
print("Access nested element:", nested[1][0])
line()

#8 Tuple Unpacking
print("Tuple Unpacking:")
person = ("Rashmin", 21, "Student")
name, age, role = person
print("Name:", name)
print("Age:", age)
print("Role:", role)
line()

#9 Combining Tuples
print("Combining Tuples:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Combined tuple:", combined)
line()

#10 Single-element Tuple (Notice the comma!)
single = (5,)    # ← must include comma!
not_tuple = (5)  # ← this is just an integer
print("Single-element tuple:", single, "type:", type(single))
print("Not a tuple:", not_tuple, "type:", type(not_tuple))
line()

# 11 Converting Between Tuple and List
print("Conversion between list and tuple:")
list_version = list(numbers)
print("Tuple to list:", list_version)
tuple_version = tuple(list_version)
print("List to tuple:", tuple_version)
line()

print(" Tuple Demo Completed!")

