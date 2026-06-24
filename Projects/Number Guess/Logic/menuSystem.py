import Logic.misc as misc
import Logic.saveSystem as save
import Logic.guessingAlgorithm as guess

def MenuLoop():

    while True:

        print(""" 
- - MENU OPTIONS - -
          
1 - Guess the number.
2 - Display stats.
3 - Save progress.
4 - Exit.

            """)
    
        choice = input("Select an option:  ")

        if choice == "1":

            print("\n - - GUESSING GAME INITIATED - -")
            guess.GuessNumber()
        elif choice == "2":

            misc.DisplayStats()            
        elif choice == "3":

            save.SaveData()
        elif choice == "4":

            print("\n\n\n - - TERMINATING PROGRAM - - \n")
            exit()
        else:

            print("\n - - INVALID OPTION - -\n")
    