#Functions
def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    bfield = field.isalpha()
    while bfield == '' or bfield == False:
        print("This field can't be blank or have numbers in it. Please try again.")
        field = input("Answer here: ")
        bfield = field.isalpha()
#Main
a = input("What's your name? ")
no_blank_fields_pls(a)
(print)