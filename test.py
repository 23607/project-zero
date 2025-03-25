import time

#Functions
def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    while field == '' or field.isalpha() == False:
        print(">Emm, I think you should answer with words.<")
        field = input("Answer again here please: ")
        if field == 'stop':
            ('Alright, I will stop')
            exit()

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
            print('Alright, I will stop')
            exit()
        else:
            print("Please enter 'yes', 'y', 'no' or 'n'. ")
            question = input('answer again here, please: ')
            questionb = question.lower()
#Main
while True:
    pname = input("Tell me, what is your name? ")
    if pname == 'stop':
        exit()
    no_blank_fields_pls(pname)
#"pname" is the player's name. This will be used later on.
    time.sleep(0.5)
    confirm_name = input(f"So, Ok... you're {pname}?")
    (print)

    if Y_or_N(confirm_name) == 'yes':
        break
    elif Y_or_N(confirm_name) == 'no':
        time.sleep(1)
        print("Oh, ok.")
print(f'Hello, {pname}')