class Rectangle:
    def __init__(self , width=0, height=0):
        self.width = width
        self.height = height
  

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Example usage:
rect = Rectangle(4,3)   
print("The  Height and Width are:", rect.height , rect.width)
print("The Area is:", rect.area())
print("The Perimeter is:", rect.perimeter())