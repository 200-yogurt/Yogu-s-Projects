import time
from config import *

def loading_time(text, amount):
    print(text)
    time.sleep(amount)
def intro_cutscene(type):
    if "new" in type:
        loading_time("\n- WELCOME . . . TO THIS EXCITING NEW ADVENTURE \n", speed["moderate"])
        loading_time("- BEFORE WE CONTINUE, I'D LIKE TO KNOW MORE ABOUT YOU...", speed["moderate"])
        loading_time("Loading. . .", speed["slow"])

        playerData["NAME"] = input("* * Type your username: * *\n")

        loading_time("\n     EXCELLENT . . . \n- SHALL WE CONTINUE?", speed["slow"])
    elif "old" in type:
        print(f"- WELCOME BACK, {playerData["NAME"]}") 
        loading_time("Loading. . .", speed["slow"])