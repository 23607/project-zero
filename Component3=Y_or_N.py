import time

#Functions
def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    while field == '' or field.isalpha() == False:
        print(">Emm, try answering with words -only-.<")
        time.sleep(0.5)

# functions
def Y_or_N(question):
    """Checks that users enter yes / y or no / n to a question"""
    questionb = question.lower()
    while True:
        if questionb == 'yes' or questionb == 'y':
            return 'yes'
        elif questionb == 'no' or questionb == 'n':
            return 'no'
        else:
            print(">Please enter 'yes', 'y', 'no' or 'n'.<")
            time.sleep(0.5)


# Main
george = input('Do you like ice cream? ')
bee = Y_or_N(george)
(print)
if bee == 'yes':
    print('This works!')
if bee == 'no':
    print('This works!')