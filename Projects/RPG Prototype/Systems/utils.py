import time
from config import *

def loading_time(text, amount):
    print(text)
    time.sleep(amount)
def intro_cutscene(type):
    if "new" in type:
        print("- WELCOME . . . TO THIS EXCITING NEW ADVENTURE \n")
        loading_time("", speed["moderate"])
        print("- BEFORE WE CONTINUE, I'D LIKE TO KNOW MORE ABOUT YOU...\n")
        loading_time("", speed["moderate"])

        playerData["NAME"] = input("* * Type your username: * *\n")
        loading_time("", speed["moderate"])

        print("     EXCELLENT . . . \n- SHALL WE CONTINUE?")
        loading_time("", speed["slow"])
    elif "old" in type:
        print(f"- WELCOME BACK, {playerData["NAME"]}") 
        loading_time("", speed["moderate"])