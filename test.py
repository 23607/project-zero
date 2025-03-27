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

#Main
while True:
    time.sleep(0.5)
    pname = input("Tell me, what is your name? ")
    if pname == 'stop':
        exit()
    elif no_blank_fields_pls(pname) == True:
#"pname" is the player's name. This will be used later on.
        time.sleep(0.5)
        confirm_name = input(f"Ok, so... you're {pname}? ")
        if Y_or_N(confirm_name) == 'yes':
            break
        elif Y_or_N(confirm_name) == 'no':
            time.sleep(1)
            print("Oh, well in that case...")
        else:
            print("Oh, pardon me, I didn't get what you said.")
    else:
        print("Oh, pardon me, I didn't get what you said.")
print(f'Hello, {pname}')