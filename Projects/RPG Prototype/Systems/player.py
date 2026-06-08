import os
from config import *
from Systems.utils import loading_time

def game_over():
    print(f"- IT SEEMS LIKE WE LOST YOU... \n- {playerData["NAME"]}! IT WAS NICE TO MEET YOU!")
    loading_time("", speed["fast"])
    print("\n\n  .  .  .  Game Over  .  .  . \n\n")
    loading_time("", speed["moderate"])

    choice = input("Would you like to start over?  (y/n)\n")
    loading_time("", speed["fast"])
    if "y" in choice:
        if os.path.exists(saveFilePath):
            os.remove(saveFilePath)
        print("\nCome back soon. . .\n")
    elif "n" in choice:
        loading_time(". . .", speed["moderate"])
        print("But aren't you dead?")
def player_status():
    if playerData["HEALTH"] > 0:
        isAlive = True
    else:
        isAlive = False

    return isAlive