#Libraries
import time
#Functions
def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    while field == '' or field.isalpha() == False:
        print(">Emm, try answering with words -only-.<")
        time.sleep(0.5)

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
print('A fine name that is')
time.sleep(1.5)
print(f"Alright, {pname}, the time has come. Your very own tale of grand adventure is about to unfold. On your journey, you will meet countless Pokémon and people.")
time.sleep(1.5)
print("I'm sure that along the way you will discover many things, perhaps even something about yourself. Now, go on, leap into the world of Pokémon!")
time.sleep(1.5)
print('...loading...')
time.sleep(1.5)
print('>You are chilling in your room, watching television<')
time.sleep(1)
print('>Suddenly, Your friend Randee comes running upstairs. He has something to tell you.<')
time.sleep(1)
print("Randee: There you are!")
time.sleep(1)
print(f'Randee: Hey, {pname}! Did you just see the TV? Sure you did!')
print("Professor Rowan's that really important guy who studies Pokémon, right?")
print('That means he must have lots and lots of Pokémon')
print("So, if we ask him, I bet he'd give us some Pokémon")
time.sleep(1)
print(">Randee stops chattering for a second to coment on your new laptop<")
time.sleep(1)
print("Randy: Were was I? Oh, right. We're going to go see Professor Rowan and get some Pokémon. I'll be waiting outside")
print("If you're late, I'll fine you $10 million!")
time.sleep(1.5)