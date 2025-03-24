#Functions
def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    bfield = field.isalpha()
    while bfield == '' or bfield == False:
        print(">Emm, I think you should answer with words.<")
        field = input("Answer again here please: ")
        bfield = field.isalpha()
#Main
a = input("What's your name? ")
no_blank_fields_pls(a)
(print)