# list.py
# This program shows how to create and use lists in Python

def line():
    print("-" * 50)

# 1 Creating Lists
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "mango"]
mixed = [25, "hello", 3.14, True]

print("Original Lists:")
print("numbers =", numbers)
print("fruits =", fruits)
print("mixed =", mixed)
line()

# 2 Accessing List Elements (Indexing)
print("Accessing elements:")
print("First fruit:", fruits[0])       # index starts from 0
print("Last fruit:", fruits[-1])       # negative index = from end
line()

# 3 Slicing (Extracting part of list)
print("Slicing examples:")
print("numbers[1:4] =", numbers[1:4])  # index 1 to 3
print("numbers[:3] =", numbers[:3])    # from start to index 2
print("numbers[2:] =", numbers[2:])    # from index 2 to end
line()

# 4 Adding Elements
print("Adding elements:")
fruits.append("orange")                # add at end
print("After append:", fruits)
fruits.insert(1, "kiwi")               # insert at specific index
print("After insert:", fruits)
line()

# 5 Removing Elements
print("Removing elements:")
fruits.remove("banana")                # remove by value
print("After remove('banana'):", fruits)
removed_item = fruits.pop()            # remove last item
print("After pop():", fruits, " (Removed:", removed_item, ")")
line()

# 6 Updating Elements
print("Updating elements:")
numbers[2] = 99
print("After update:", numbers)
line()

# 7 Looping through List
print("Loop through fruits:")
for fruit in fruits:
    print(fruit)
line()

# 8 List Functions
print("Common List Functions:")
print("Length:", len(numbers))          # number of elements
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
line()

# 9 Sorting and Reversing
print("Sorting and reversing:")
numbers.sort()       # ascending order
print("Sorted:", numbers)
numbers.reverse()    # reverse order
print("Reversed:", numbers)
line()

# 10 Nested Lists (List inside another list)
print("Nested List Example:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix =", matrix)
print("Access middle element:", matrix[1][1])
line()

# 11 Copying Lists
print("Copying lists:")
list_copy = fruits.copy()
print("Copied list:", list_copy)
line()

# 12 Combining (Concatenating) Lists
print("Combining lists:")
combined = numbers + [100, 200]
print("Combined list:", combined)
line()

print(" List Demo Completed!")
