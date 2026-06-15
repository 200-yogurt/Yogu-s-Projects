import config
import random
from config import *
from Systems.utils import narrate

def explore():  

    stats = config.playerData["stats"]

    def find_gold():

        narrate("\nYou explored in search for Gold and...", speed["slow"])

        randomNum = random.randint(0, 50)

        if randomNum > 0:
            stats["GOLD"] += randomNum

            print("You found Gold!")
            narrate("Loading. . .", speed["fast"])
            print(f"- CONGRATULATIONS ADVENTURER, YOU FOUND {randomNum:03} GOLD")
        else:
            narrate("found nothing...", speed["moderate"])
            print("- . . . UNLUCKY")

    def lose_health():

        narrate("\nYou explored in the wilderness and...", speed["slow"])

        randomNum = random.randint(0, stats["HEALTH"])

        if randomNum > 0:
            stats["HEALTH"] -= randomNum

            print("You got attacked by a creature!")
            narrate("Loading. . .", speed["fast"])
            print(f"- OUCH. . . YOU LOST {randomNum} HP")
        else:
            print("Nothing happened")

    def healing_herb():

        narrate("\nYou explored in the wilderness and...", speed["slow"])

        randomNum = round(random.uniform(1, stats["HEALTH"] * 0.87))

        stats["HEALTH"] += randomNum

        print("You found a Healing Herb!")
        narrate("Loading. . .", speed["fast"])
        print(f"- CONGRATULATIONS ADVENTURER, YOU GAINED {randomNum} HP")
    
    def nothing_happens():
        
        narrate("\nYou explored...", speed["slow"])
        print("but nothing relevant happened")

    events = [
        find_gold,
        lose_health,
        healing_herb,
        nothing_happens
    ]

    choosenEvent = random.choice(events)
    choosenEvent()
