# dictionary_demo.py
# This program demonstrates how dictionaries work in Python.

def line():
    print("-" * 50)

# Creating a dictionary
student = {
    "name": "Rashmin",
    "age": 20,
    "course": "Python",
    "marks": 85
}

print("Original Dictionary:")
print(student)
line()

# Accessing values
print("Accessing values using keys:")
print("Name:", student["name"])
print("Course:", student.get("course"))   # safer way
line()

# Adding new key-value pairs
print("Adding new key-value pair:")
student["email"] = "rashmin@example.com"
print(student)
line()

# Updating existing values
print("Updating existing value:")
student["marks"] = 90
print(student)
line()

# Removing elements
print("Removing elements:")
student.pop("age")             # remove by key
print("After pop('age'):", student)

del student["course"]          # delete a key manually
print("After del student['course']:", student)

student.clear()                # remove all key-value pairs
print("After clear():", student)
line()

# Recreate dictionary for next examples
student = {
    "name": "Rashmin",
    "age": 20,
    "course": "Python",
    "marks": 90
}

# Looping through dictionary
print("Looping through dictionary:")
for key in student:
    print(f"Key: {key}, Value: {student[key]}")
line()

# Viewing all keys, values, and items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items (key-value pairs):", student.items())
line()

# Nested dictionary
print("Nested Dictionary Example:")
students = {
    "student1": {"name": "Rashmin", "marks": 90},
    "student2": {"name": "Karan", "marks": 85}
}
print(students)
print("Accessing nested data:", students["student2"]["marks"])
line()

# Dictionary comprehension
print("Dictionary Comprehension Example:")
squares = {x: x**2 for x in range(1, 6)}
print(squares)
line()

print("Dictionary demonstration completed.")

