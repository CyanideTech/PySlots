import random
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

yes = ("yes", "y", "YES", "Y", "Yes", "yEs", "YeS", "yES")
money = 1000

game = input("Welcome to PySlots! What game would you like to play? Classic or Career? ")

if game.lower() == "classic":
    print("Welcome to Classic! You start with $1000.")
    while True:
        bet = int(input("How much would you like to bet? "))
        if bet <= money:
            outcomes = ["Win", "Loss"]
            result = random.choices(outcomes)[0]
            print(f"The result is: {result}")

            if result == "Win":
                money += bet
            else:
                money -= bet

            print(f"You now have: ${money}")
        else: 
            print("You do not have that much money.")
    

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

else:
    print("Welcome to Career! You start with $1000.")

    weights = [90, 10]
    while True:
        bet = int(input("How much would you like to bet? "))
        if bet <= money:
            outcomes = ["Win", "Loss"]
            result = random.choices(outcomes, weights=weights, k=1)[0]
            print(f"The result is: {result}")

            if result == "Win":
                money += bet
                weights = [w + d for w, d in zip(weights, [-10, 10])]
            else:
                money -= bet

            print(f"You now have: ${money}")
        else: 
            print("You do not have that much money.")
    

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