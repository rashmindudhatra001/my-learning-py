# Taking marks as input from user
marks = int(input("Enter your marks: "))



# Checking conditions for grades
if marks >= 80:
    print("You have received A grade") 
elif marks >= 60:
    print("You have received B grade")
elif marks >= 40:   
    print("You have received C grade")
else:
    print("You have received F grade")  