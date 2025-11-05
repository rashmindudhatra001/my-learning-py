def outer_funcation():
    x = 1 # outer variable
    
    def inner_function():
        y = 2 # inner variable]
        result = x + y
        return result
    
    return inner_function()
   
output = outer_funcation()