# Taking marks as input from user
english_marks =int(input("Enter your English marks:"))
maths_marks =int(input("Enter your Maths marks:"))

# Checking conditions for grades
if english_marks > 80 and maths_marks > 80:
    print("You have received A grade")
elif english_marks > 80 or maths_marks > 80:
    print("You have received B grade")
else:
    print("You have received C grade")