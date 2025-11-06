class Parent:

    def __init__(self):
        print("Hello from Parent" )
        
        
class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Hello from Child" )
        
        
        
        
child1 = Child()
                 
    