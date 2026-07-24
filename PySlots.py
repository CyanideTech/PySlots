import random
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

yes = ("yes", "y")
money = 1000

clear()

game = input("Welcome to PySlots! What game would you like to play? Classic or Career? ").strip().lower()

if game == "classic":
    print("Welcome to Classic! You start with $1000.")

    while True:
        bet_input = input("Enter bet (or 'q' to quit): ").strip().lower()

        if bet_input == 'q':
            print("Thanks for playing PySlots! Goodbye!")
            sys.exit()

        try:
            bet = int(bet_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
            
        if bet > money:
            print("You do not have that much money.")
            continue
            
        result = random.choice(["Win", "Loss"])
        print(f"The result is: {result}")
        
        if result == "Win":
            money += bet
        else:
            money -= bet
            
        print(f"You now have: ${money}")
        
        if money <= 0:
            print("GAME OVER! You have no more money left.")
            play_again = input("Would you like to play again? (yes/no): ").strip().lower()
            if play_again in yes:
                clear()
                money = 1000
                print("You now have $1000 to play with!")
            else:
                print("Thanks for playing PySlots! Goodbye!")
                sys.exit()
                
elif game == "career":
    print("Welcome to Career! You start with $1000.")
    
    weights = [90, 10]  # [Win, Loss]
    
    while True:
        bet_input = input("Enter bet (or 'q' to quit): ").strip().lower()
        
        if bet_input == 'q':
            print("Thanks for playing PySlots! Goodbye!")
            sys.exit()
            
        try:
            bet = int(bet_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
            
        if bet > money:
            print("You do not have that much money.")
            continue
            
        result = random.choices(["Win", "Loss"], weights=weights, k=1)[0]
        print(f"The result is: {result}")
        
        if result == "Win":
            money += bet
            # make game harder safely
            weights[0] = max(0, weights[0] - 10)   # decrease win chance
            weights[1] = min(100, weights[1] + 10) # increase loss chance
        else:
            money -= bet
            
        print(f"You now have: ${money}")
        print(f"(Win chance: {weights[0]}%, Loss chance: {weights[1]}%)")
        
        if money <= 0:
            print("GAME OVER! You have no more money left.")
            play_again = input("Would you like to play again? (yes/no): ").strip().lower()
            if play_again in yes:
                clear()
                money = 1000
                weights = [90, 10]
                print("You now have $1000 to play with!")
            else:
                print("Thanks for playing PySlots! Goodbye!")
                sys.exit()
                
else:
    print("Invalid game mode selected. Please restart and choose 'Classic' or 'Career'.")
