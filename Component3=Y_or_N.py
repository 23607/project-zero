# functions
def Y_or_N(question):
    """Checks that users enter yes / y or no / n to a question"""
    questionb = question.lower()
    while True:
        if questionb == 'yes' or questionb == 'y':
            return 'yes'
        elif questionb == 'no' or questionb == 'n':
            return 'no'
        elif questionb == 'stop':
            print('The program has been stopped')
            break
        else:
            print("Please enter 'yes', 'y', 'no' or 'n'. ")
            question = input('answer again here, please: ')
            questionb = question.lower()

# Main
george = input('Do you like ice cream? ')
bee = Y_or_N(george)
(print)
if bee == 'yes':
    print('This works!')
if bee == 'no':
    print('This works!')