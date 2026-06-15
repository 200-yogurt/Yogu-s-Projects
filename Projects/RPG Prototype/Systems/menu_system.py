import config
from config import *
from Systems.utils import narrate
from Systems.player import inventory_add
from Systems.explore_system import explore
from Systems.save_system import save_player_data


def display_stats():

    narrate("- HAVE A PEEK AT YOUR STATS . . .\n", speed["fast"])

    for key, value in config.playerData["stats"].items():
        print(f"{key} : {value}")
        
def display_inventory():

    narrate("- HAVE A PEEK AT YOUR INVENTORY . . .\n", speed["fast"])

    for value in config.playerData["inventory"]:
        print(f"{value}")

def rest():
    
    stats = config,playerData["stats"]

    restGoldCost = 10
    restHealAmount = 25 # Adding unique variables for the Rest feature since I plan to expand further upon this in the future

    if stats["GOLD"] >= restGoldCost:
        stats["HEALTH"] += restHealAmount 
        stats["GOLD"] = stats["GOLD"] - restGoldCost 
    if stats["GOLD"] >= restGoldCost:
        stats["HEALTH"] += restHealAmount 
        stats["GOLD"] = stats["GOLD"] - restGoldCost 

        print("\nSuccesfully Rested")
    else:
        print("- YOU DON'T SEEM TO HAVE ENOUGH RESOURCES, ADVENTURER...")

def save_progress():

    choice = input(f"- ARE YOU SURE YOU WANT TO REWRITE YOUR SAVE, ADVENTURER?  (y/n)\n").strip().lower()
    narrate("Loading. . .", speed["slow"])

    if "y" in choice:
        save_player_data()

        print("Saved Succesfully")
    elif "n" in choice:
        print("Aborted")
    else:
        print("Invalid Option")

def quit():

    narrate("- UNTIL NEXT TIME, ADVENTURER", speed["slow"])
    narrate("\n\n  .  .  .  Terminating Program  .  .  . \n\n", speed["slow"])

    exit()


def menu_loop():

    print(f"""
- WELCOME TO THE MENU, {    config.playerData["stats"]["NAME"]   }

    0.0 - Inventory Add
    1- View Stats
    2- View Inventory
    3- Rest (costs 10$)
    4- Explore
    5- Save
    6- Quit

- WHAT DO YOU DESIRE THIS TIME, ADVENTURER?
          """)
    narrate("Loading. . .", speed["fast"])

    choice = input("Please choose a number between 1 and 6 in order to continue: \n").strip()
    if choice == "1":
        display_stats()
    elif choice == "0":
        inventory_add(21)
    elif choice == "2":
        display_inventory()
    elif choice == "3":
        rest()
    elif choice == "4":
        explore()
    elif choice == "5":
        save_progress()
    elif choice == "6":
        quit()
    else:
        print("Invalid Option")

    narrate("", speed["slow"])