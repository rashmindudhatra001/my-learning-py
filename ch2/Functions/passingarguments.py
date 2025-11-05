#pass by value

def addOne(x):
    x += 1
    print("Inside addOne function:", x)
    
x = 5   
addOne(x)
print("Outside addOne function:", x)  # x remains unchanged



#pass by reference

def modifyList(lst):
    lst.append(4)
    print("Inside modifyList function:", lst)
    
    
    
myList = [1, 2, 3]
modifyList(myList)
print("Outside modifyList function:", myList)  # myList is modified       
