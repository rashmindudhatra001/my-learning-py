# Set Demo in Python
# This program demonstrates how sets work in Python.

def line():
    print("-" * 50)

# 1 Creating Sets
numbers = {10, 20, 30, 40, 50}
fruits = {"apple", "banana", "mango"}
mixed = {1, "hello", 3.14, True}

print("Original Sets:")
print("numbers =", numbers)
print("fruits =", fruits)
print("mixed =", mixed)
line()

# 2 No Duplicates Allowed
print("Duplicate values are removed automatically:")
dup_set = {1, 2, 2, 3, 3, 4, 4}
print("dup_set =", dup_set)
line()

# 3 Adding Elements
print("Adding elements:")
fruits.add("orange")           # Add a single element
print("After add:", fruits)

fruits.update(["grape", "kiwi"])  # Add multiple elements
print("After update:", fruits)
line()

# 4 Removing Elements
print("Removing elements:")
fruits.remove("banana")        # Remove element (Error if not found)
print("After remove('banana'):", fruits)

fruits.discard("apple")        # Remove element safely (no error)
print("After discard('apple'):", fruits)

removed_item = fruits.pop()    # Removes random element
print("After pop():", fruits, " (Removed:", removed_item, ")")

fruits.clear()                 # Removes all elements
print("After clear():", fruits)
line()

# 5 Recreate fruits for next steps
fruits = {"apple", "banana", "mango", "orange"}

# 6 Set Operations
print("Set Operations:")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("A =", A)
print("B =", B)

print("Union (A | B) =", A | B)                    # All elements (no duplicates)
print("Intersection (A & B) =", A & B)             # Common elements
print("Difference (A - B) =", A - B)               # Elements in A not in B
print("Symmetric Difference (A ^ B) =", A ^ B)     # Elements not in both
line()

# 7 Membership Test
print("Membership test:")
print("2 in A ->", 2 in A)
print("10 not in B ->", 10 not in B)
line()

# 8 Set Functions
print("Useful Set Functions:")
print("Length of A:", len(A))
print("Max of A:", max(A))
print("Min of A:", min(A))
print("Sum of A:", sum(A))
line()

# 9 Frozen Set (Immutable set)
print("Frozen set example:")
fset = frozenset({1, 2, 3, 4})
print("Frozen set:", fset)
# fset.add(5)  # ❌ This will cause an error (cannot modify)
line()

print(" Set Demo Completed!")
