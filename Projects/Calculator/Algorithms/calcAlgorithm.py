def Calculate():

    functional_operators = [
        "+",
        "-",
        "*",
        "/"
    ]

    number1 = float(    input(  "Enter digit:  ").strip())
    operator = input(   "Enter operator:  ").strip()
    number2 = float(    input(  "Enter digit:  ").strip())

    if operator not in functional_operators:

        print("\n- - Invalid operator - -")
        return


    if "+" in operator:

        result = number1 + number2 
    elif "-" in operator:

        result = number1 - number2
    elif "*" in operator:

        result = number1 * number2
    elif "/" in operator:

        if number2 == 0.0:

            print("\n - - Math error - -")
            return
        
        result = number1 / number2        

    print(f"Result: {   result  }")
