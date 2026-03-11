import random
import sys
import os

print("Welcome to PySlots! You start with $1000.")

yes = ("yes", "y", "YES", "Y", "Yes", "yEs", "YeS", "yES")
money = 1000

while True:
    bet = int(input("How much would you like to bet? "))

    outcomes = ["Win", "Loss"]
    result = random.choice(outcomes)
    print(f"The result is: {result}")

    if result == "Win":
        money += bet
    else:
        money -= bet

    print(f"You now have: ${money}")

    if money <= 0:
        print("GAME OVER! You have no more money left.")
        play_again = input("Would you like to play again? (yes/no)")
        if play_again in yes:
            os.system('cls' if os.name == 'nt' else 'clear')
            money = 1000
            print("You now have 1000 dollars to play with!")
        else:
            print("Thanks for playing PySlots! Goodbye!")
            sys.exit()
