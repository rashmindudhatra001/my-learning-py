#for converting string to upper case
name1 = "Rayshmin Patel"
name2 = name1.upper()
print("Uppercase String:", name2)
print("Original String remains unchanged:", name1)

#for converting string to lower case
name3 = name2.lower()
print("Lowercase String:", name3)
print("Original String remains unchanged:", name2)


#for capitalize first letter of string
name4 = name3.capitalize()
print("Capitalized String:", name4)
print("Original String remains unchanged:", name3)


#for striping whitespace from string    
name5 = "   Hello World!   "
print("Original String with whitespaces:", repr(name5))
name6 = name5.strip()
print("String after striping whitespaces:", repr(name6))



#for replacing substring in string
story = "Once upon a time, there was a king. The king was very kind."
new_story = story.replace("king", "queen")
print("Modified Story:", new_story)
print("Original Story remains unchanged:", story)   




#for splitting a string into list of substrings
sentence = "Python is a great programming language"
words = sentence.split(" ")
words1 = sentence.split(" " , 2)  #maxsplit=2
print("List of words with maxsplit=2:", words1)
print("List of words:", words)
print("Original Sentence remains unchanged:", sentence)






#concatenation of strings
first_name = "Rayshmin"
last_name = "Patel"
full_name = first_name + " " + last_name
print("Full Name:", full_name)  



#string formatting
age = 25
height = 5.9
info = "My name is {}. I am {} years old and my height is {} feet.".format(full_name, age, height)
print(info)