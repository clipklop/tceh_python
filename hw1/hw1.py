# Riddle game


import random

riddle_list = {
    "What is best material music carrier?": "vinyl",
    "What is the first word that baby supposed to say first?": "mama",
    "Famous animal of Schrodinger expirement": "cat",
    "How americans calls a Football game?": "soccer",
    "What is name of mobile operation system developed by Google inc?": "android",
    "'The winter is coming!' - which family House says so?": "starks",
    "Finish one of the best advices 'Don't invent the ...'": "wheel",
    "At the dawn of internet we used to chat in IRC, but every geeks uses what?": "slack",
    "What is the name of Linux inventor?": "linus",
    "What is symbol operator of 'intersection' of Python data type 'set'": "&",
 }

def game():
    print("""
                    Welcome to the Riddle game.
                                ---
        --
        You have to answer on riddles questions one by one.
        Or if you are silly just press 'q' or write down 'quit' to leave.
        ---
        """)
    wrong_counter = 3
    print("You've {} attempts to riddle it!".format(wrong_counter))
    for k, v in riddle_list.items():
            answer = input("{} ".format(k)).lower()
            if answer == v:
                print("Alright! That's right. Keep it up!")
                continue
            elif answer == 'q' or answer == 'quit':
                print("Bye!")
                break
            else:
                wrong_counter -= 1
                print("Wrong. You have {} attempts left.".format(wrong_counter))
                print("The right answer is {}".format(v))
                if wrong_counter <= 0:
                    print("Sorry, you lose.")
                    break
                continue
    else:
        print("Congratz! You've riddle it all!")


game()