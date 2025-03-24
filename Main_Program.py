#Libraries
import time
#Functions
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
            question = input('>Psst, player, the question was yes or no, answer again here, please<: ')
            questionb = question.lower()
    
def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    bfield = field.isalpha()
    while bfield == '' or bfield == False:
        print(">Emm, I think you should answer... with words :D.<")
        field = input("Answer again here please: ")
        bfield = field.isalpha()

#Main code
print("Hello there! It's so very nice to meet you! Welcome to the world of Pokémon!")
time.sleep(1.5)
print("My name is Rowan. However, everyone just calls me the Pokémon Professor. This world is widely inhabited by creatures known as Pokémon.")
time.sleep(1.5)
print("Here, I have a Poké Ball. Touch the button on the middle of the Poké Ball, if you'd please.")
time.sleep(1)
print('.')
time.sleep(0.5)
print('..')
time.sleep(0.5)
print('...')
time.sleep(0.5)
print(">POP! A Pokémon came out of the Pokeball!<")
time.sleep(1.5)
name_correct = False
while name_correct == False:
    pname = input("Tell me, what is your name? ")
    no_blank_fields_pls(pname)
#"pname" is the player's name. This will be used later on.
    time.sleep(0.5)
    confirm_name = input(f"So, Ok... you're {pname}?")
    Y_or_N(confirm_name)
    (print)
    if Y_or_N == 'yes':
        name_correct = True
    elif Y_or_N == 'no':
        time.sleep(1)
        print("Oh, ok.")
            
