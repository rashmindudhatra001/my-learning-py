

class Animal:
    def speaks(self):
        pass
    
    
class Dog(Animal):
    def speaks(self):
        print("Woof!")
        

class Cat(Animal):
    def speaks(self):
        print("Meow!")
        
        
        
class Cow(Animal):
    def speaks(self):
        print("Moo!")
        
        
        
dog = Dog()
cat = Cat()
cow = Cow()


dog.speaks()  # Output: Woof!
cat.speaks()  # Output: Meow!
cow.speaks()  # Output: Moo!        
        
        
        
                    