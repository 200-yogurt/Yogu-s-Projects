import os
import json
import Data.settings as settings

save_file_path = "Data/save.json"

def SaveData():

    with open(save_file_path, "w", encoding="utf-8") as file:

        json.dump(settings.stored_data, file, indent= 4)

def LoadData():

    if os.path.exists(save_file_path):

        with open(save_file_path, "r") as file:

            settings.stored_data = json.load(file)

    else:

        with open(save_file_path, "x") as file:

            SaveData()

