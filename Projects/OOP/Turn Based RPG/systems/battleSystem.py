from utils import *
from classes.player import Player
from classes.enemy import Enemy

def start__():

    narrate__("\n\n=== BATTLE INITIALIZED ===\n\n", slow)

    player = Player("Yogu", 10, 10)
    enemy = Enemy("Slime", 25, 5)
    battle_turn = 0

    narrate__(f"// {player.name} // VS // {enemy.name} //", moderate)
    narrate__(". . . Begin!\n\n", fast)

    while True:

        battle_turn += 1
        narrate__(f"\n== Turn:  {battle_turn}\n", fast)

        narrate__("----------------------------------------", fast)

        print("== Current Stats ==\n")
        player.display_stats__()
        enemy.display_stats__()

        narrate__("Loading . . .\n", moderate)

        if player.health <= 0:

            narrate__("\n== You collapsed... You Lost ==\n", moderate)
            narrate__("----------------------------------------", fast)

            break
        else:

            narrate__("== Select an option: \n\n 1. Attack\n", fast)
            choice = input(" - Option: ")

            if choice == "1":

                player.attack__(enemy)
        if enemy.health <= 0:

            narrate__("\n== The Enemy has fainted... You Win! ==\n", moderate)
            narrate__("----------------------------------------", fast)

            break
        else:

            enemy.attack__(player)

        narrate__("----------------------------------------", fast)