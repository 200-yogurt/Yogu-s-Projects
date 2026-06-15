import time
import config
from config import *

def narrate(text, amount):

    print(text)
    time.sleep(amount)
    
def intro_cutscene(type):

    if "new" in type:

        narrate("\n- WELCOME . . . TO THIS EXCITING NEW ADVENTURE \n", speed["moderate"])
        narrate("- BEFORE WE CONTINUE, I'D LIKE TO KNOW MORE ABOUT YOU...", speed["slow"])
        narrate("Loading. . .", speed["fast"])

        config.playerData["stats"]["NAME"] = input("* * Type your username: * *\n")

        narrate("\n     EXCELLENT . . . \n- SHALL WE CONTINUE?", speed["slow"])
    elif "old" in type:
        
        print(f"- WELCOME BACK, {   config.playerData["stats"]["NAME"]  }") 
        narrate("Loading. . .", speed["slow"])