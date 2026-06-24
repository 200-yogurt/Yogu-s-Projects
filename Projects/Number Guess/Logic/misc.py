import Data.settings as settings

def DisplayStats():

    print(f"""
 - - DISPLAYING STATS - -
          
        Current Status:
 - Attempts: {   settings.stored_data["attempts"]    }
 - Correct guesses: {  settings.stored_data["wins"]    }
          """)