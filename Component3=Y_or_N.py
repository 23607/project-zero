# functions
def Y_or_N(question):
    """Checks that users enter yes / y or no / n to a question"""
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes" 
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")


# Main
# loop for testing
