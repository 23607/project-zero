answered = False
question = input("do you like skibidi ").lower()
while answered == False:
    if question == "yes":
        print("what,,,,,,")
        answered = True
    elif question == "no":
        print("good")
        answered = True
    else:
        print("that's not an answer, say yes or no, you bozo")
        input(question)

