# 9. Write a program using OOP: Define a class Person with attributes name, age; then subclass Student which adds course and marks. Include a method to display student details.




class Person:
    def __init__  (self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    
    
    
    
class Student (Person):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course = course
        self.marks = marks
        
    def __str__(self):
        return f"{super().__str__()}, Course: {self.course}, Marks: {self.marks}"   
    
    
    


student = Student("asdf", 23, "asdfg", 43)
print(student)         






























