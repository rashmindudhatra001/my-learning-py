import random

low = 1 
high = 100
ans = random.randint( low , high)
guesses = 0
is_runing = True

print("Python Number Guessing Game")
print(f"Select a number between {low} and {high}")

while is_runing:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int (guess)
        guesses += 1
        
        if guess < low or guess > high:
            print("that number is out of range")
            print(f"Select a number between {low} and {high}")
            
        elif guess < ans:
            print ("Too Low! Try again")
            
        elif guess > ans:
            print ("Too haigh! Try again")
            
        else:
            print(f"CORRECT! The answeras: {ans}")
            print(f"Number of guesss: {guesses} ")  
            is_runing = False  
    else:
        print("Invalid guess")
        print(f"Select a number between {low} and {high}")
