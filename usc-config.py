""" textAdventure.py
Erica Weems
09/15/2017
Text adventure game with functions and inventory
"""
#My global variables and initial values
lives = 3
points = 0
#points = [magenta, cyan, yellow, white]
status = "alive"

#My functions
def start():
    user = raw_input("what do you enjoy?")
    print user
"""def dead():
    if status != alive:
        print "You have died. You have " + lives + " left."
            #if lives > 0:
                #print "Let's try again."
            #    start()
            else:
                again = raw_input("Like, suuuupppperrrrr dead. Wanna start over?")
                if again.upper() == "Y" or again.upper() == "YES":
                    print "Let's go!"
                    start() #startover()?
            else:
                print "Goodbye!"
                quit()"""

#My loops




#The rest
start()
