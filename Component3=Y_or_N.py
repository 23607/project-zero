# functions
def Y_or_N(question):
    """Checks that users enter yes / y or no / n to a question"""
    question = question.lower()
    while True:
        if question == 'yes' or 'y':
            return 'yes'
        elif question == 'no' or 'n':
            return 'no'
        else:
            print("Please enter 'yes', 'y', 'no' or 'n'. ")

# Main
george = input('Do you like what it doeas to your blemis? ')
bee = Y_or_N(george)
(print)
if bee == 'yes':
    print('This works!')