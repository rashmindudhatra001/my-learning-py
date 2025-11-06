class student:
    
    def name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name   
    
student1 = student()
student1.name("Alice")
print(student1.get_name())  # Output: Alice      