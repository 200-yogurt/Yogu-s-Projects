import random
from config import *
from Systems.utils import loading_time

def explore():
    def find_gold():
        print("\nYou explored in search for Gold and...")
        loading_time("", speed["slow"])

        randomNum = random.randint(0, 50)

        if randomNum > 0:
            playerData["GOLD"] += randomNum

            print("You found Gold!")
            loading_time("", speed["fast"])
            print(f"- CONGRATULATIONS ADVENTURER, YOU HAVE FOUND {randomNum:03} GOLD")
        else:
            print("found nothing...")
            loading_time("", speed["moderate"])
            print("- . . . UNLUCKY")
    def lose_health():
        print("\nYou explored in the wilderness and...")
        loading_time("", speed["slow"])

        randomNum = random.randint(0, playerData["HEALTH"])

        if randomNum > 0:
            playerData["HEALTH"] -= randomNum

            print("You got attacked by a creature!")
            loading_time("", speed["fast"])
            print(f"- OUCH. . . YOU HAVE LOST {randomNum} HP")
        else:
            print("Nothing happened")
    def healing_herb():
        print("\nYou explored in the wilderness and...")
        loading_time("", speed["slow"])

        randomNum = round(random.uniform(1, playerData["HEALTH"] * 0.87))

        playerData["HEALTH"] += randomNum

        print("You found a Healing Herb!")
        loading_time("", speed["fast"])
        print(f"- CONGRATULATIONS ADVENTURER, YOU HAVE GAINED {randomNum} HP")
    def nothing_happens():
        print("\nYou explored...")
        loading_time("", speed["slow"])
        print("but nothing relevant happened")

    events = [
        find_gold,
        lose_health,
        healing_herb,
        nothing_happens
    ]

    choosenEvent = random.choice(events)
    choosenEvent()
