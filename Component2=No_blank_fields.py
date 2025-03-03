#Functions
def heatmor (fild):
    '''This will detect if there is any number in a field'''
    return any(num.isdigit() for num in fild)

def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    bfield = heatmor(field)
    while field == '' or bfield == True:
        print("This field can't be blank or have numbers in it. Please try again.")
        field = input("Answer here: ")
#Main
a = input("What's your name? ")
no_blank_fields_pls(a)
(print)