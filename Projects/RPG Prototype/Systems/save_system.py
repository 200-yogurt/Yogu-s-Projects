import os
import json
import config
from Systems.utils import *

def save_player_data():
    
    with open(saveFilePath, "w") as file:
        json.dump(config.playerData, file, indent=4)

def load_save_data():

    if os.path.exists(saveFilePath):
        
        with open(saveFilePath, "r") as file:
            config.playerData = json.load(file)

        print("\nSuccesfully Found & Loaded Save File")
        narrate("Loading. . .", speed["slow"])

        intro_cutscene("old")
    else:
        intro_cutscene("new")

        with open(saveFilePath, "x") as file:
            save_player_data()
