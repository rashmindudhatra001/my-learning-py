#creating a string
name1 = "Rayshmin"
name2 = 'patel'
name3 = '''dudhatra''' 

print(name1 , name2 , name3)

print(type(name1))
print(type(name2))
print(type(name3))  

#multiline string
story = '''once upon a time
there lived a king
who had a queen'''  
print(story)
print(type(story))


#travering a string

for char in name1:
    print(char)
    
    
    
#find length of string
print(len(name1))
print(len(story))
print("Length of name2 is:", len(name2))
print("Length of name3 is:", len(name3))
print("Length of story is:", len(story))



#find a substring in a string
print("is 'Ray' present in name1?", 'Ray' in name1)
print("is 'king' present in story?", 'king' in story)
print("is 'queen' present in story?", 'queen' in story)
print("is 'prince' present in story?", 'prince' in story)    


#slicing of string
print(name1[0:3])  #0,1,2
print(name1[3:7])  #3,4,5,6
print(name1[:4])   #0,1,2,3 
print(name1[-4:])   #4,5,6,7



