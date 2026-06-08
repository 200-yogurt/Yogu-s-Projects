import os
from config import *
from Systems.utils import loading_time

def game_over():
    loading_time(".....", speed["fast"])
    loading_time("- IT SEEMS LIKE WE LOST YOU... \n", speed["moderate"])
    print(f"- {playerData["NAME"]}! IT WAS NICE TO MEET YOU!")
    loading_time(".....", speed["moderate"])

    loading_time("\n\n  .  .  .  Game Over  .  .  . \n\n", speed["slow"])

    choice = input("Would you like to start over?  (y/n)\n")
    loading_time("Loading. . .", speed["slow"])
    if "y" in choice:
        if os.path.exists(saveFilePath):
            os.remove(saveFilePath)
        print("\nCome back soon. . .\n")
    elif "n" in choice:
        loading_time(". . .", speed["moderate"])
        print("But aren't you dead?")
    loading_time("", speed["slow"])
def player_status():
    if playerData["HEALTH"] > 0:
        isAlive = True
    else:
        isAlive = False

    return isAlive