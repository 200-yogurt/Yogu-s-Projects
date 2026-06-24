from Algorithms.calcAlgorithm import Calculate

def MenuDisplay():

    running = True

    while running:
        print("""
    1- Calculate
    2- Exit
              """)
        
        choice = input("Please choose a number from 1 - 2:  ").strip()

        if "1" in choice:

            print("\n- - Calculation process initiated - -\n")
            Calculate()
        elif "2" in choice:

            print("\n     Terminating Program\n")
            running = False
        else: 

            print("\n- - Invalid option - -")

    if not running:

        exit()
