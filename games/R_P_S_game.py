import random

option = ("rock", "papre", "scisors")

playing = True

while playing:
    
    player = None
    computer = random.choice(option)
    
    while player not in option:
        player = input("Enter a choice  (rock, papre, scisors): ")
        
    print(f"player: {player}")
    print(f"computer: {computer}")


    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scisors":
        print("You win!")  
        
    elif player == "papre" and computer == "rock":
            print("You win!")  

    elif player == "scisors" and computer == "papre":
            print("You win!")  
            
    else:
        ("You lose!")    
        
    if not input("Play Again? (y/n)").lower() == "y":
        playing = False
        
print("Thanks For Playing!")        
        
        
        
    

    
