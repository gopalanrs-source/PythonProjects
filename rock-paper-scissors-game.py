# rock-paper-scissors-game
import random
import sys
from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

 
print("Welcome to Rock-Paper-Scissors Game! \n")
Player_choice = int(input("Enter you choice (1 for Rock, 2 for Paper, 3 for Scissors ): \n"))
if Player_choice <1 or Player_choice > 3:
    print("Invalid choice. Please choose 1 or 2 or 3 \n  Retry again")
    sys.exit()

Computer_choice = random.randint(1,3)

if Player_choice == Computer_choice:
    print("🤣 It's a Tie!")
elif (Player_choice == Choice.ROCK and Computer_choice == Choice.SCISSORS) or (Player_choice == Choice.PAPER and Computer_choice == Choice.ROCK) or (Player_choice == Choice.SCISSORS and Computer_choice == Choice.PAPER):
    print("🎉 You Win!")
else:
    print("😞 Computer Wins!")

#print(f"Your choice: {Player_choice} | Computer's choice: {Computer_choice}")
print("You chose : "+Choice(Player_choice).name + " | Computer Chose : "+ Choice(Computer_choice).name)
print("Thanks for playing! Goodbye! \n")


