# Taking cost price and selling price as input from user
cp = int(input ("Enter the cost price: "))
sp = int(input ("Enter the selling price: "))


# Calculating profit
if sp > cp:
    print ("You made a profit of:", sp - cp)    
         
#   Calculating loss  
elif sp < cp:
    print ("You incurred a loss of:", cp - sp)     
    
 #  No profit no loss case   
else:
    print ("No profit no loss")         