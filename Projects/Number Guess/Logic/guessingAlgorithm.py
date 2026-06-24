import random
import Data.settings as settings

def GuessNumber():

    is_running = True

    print("\n!.! - To exit the current game, write 'esc' ")

    while is_running:

        print("\n\nPick a number from 1 - 10...\n")

        generated_number = str(random.randint(1, 10))
        choice = input("Your choice:  ").strip().lower()

        if choice == "esc":

            is_running = False
            return

        print(f"The number was: {generated_number}")

        if choice == generated_number:
                
            settings.stored_data["wins"] += 1
            print("...You guessed the right number!!")
        else:

            print(". . .You guessed the wrong number")

        settings.stored_data["attempts"] += 1
