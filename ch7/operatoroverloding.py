class ComplexNumber:
    
    def __init__(self, real=0, imag=0):
        self.real = real    
        self.imag = imag
        
        
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
c3 = c1 + c2

print(c3.real , "+ i" , c3.imag)  # Output: 6 + i8  