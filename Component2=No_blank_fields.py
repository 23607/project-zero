#Functions
def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    if field == '':
        print("This field can't be blank. Please, fill it and try again.")
#Main
a = input("What's your name? ")
no_blank_fields_pls(a)
(print)