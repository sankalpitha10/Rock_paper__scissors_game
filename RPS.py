import random

player =  input("player selected(rock , paper, scissors):")
computer = random.choice(['rock', 'paper', 'scissors'])
print("computer selected:", computer)

if player == computer:
    print("Tie")
elif player == 'rock':
    if computer == 'paper':
       print("Computer won the game")
    else:
        print("Player won the game")   
elif player == 'paper':
    if computer == 'scissors':
       print("computer won the game")
    else:
        print("player won the game")   
elif player == 'scissors':
    if computer == 'rock': 
       print("computer won the game")
else:
    print("player won the game")
    