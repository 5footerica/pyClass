"""  lostInSpace.py
     A Text based style adventure game
     You're a ferret trying to keep from getting caught
     by your owner
     """
import time

"""
 Start Game:  Describes scenario and goals. Sets initial key variables.
"""

start_mission = """
    You are an astronaut on a mission! your goal is to
    gather samples of soil, plant, and water if possible
    and return home.
    You've safely landed and have exited the ship. Time to explore.
    Where would you like to head first?
    """
print start_mission

def gamestart():
    global choice
    global lifenumber
    if lifenumber == 0:
        print "You've used up all your lives, you're dead. See you around, space cowboy."
        time.sleep(3)
        quit()
    global samples
    if samples >= 3:
        print "You have enough samples, time to go home. See you around, space cowboy!"
        time.sleep(3)
        quit()
    select = raw_input("Press 'l' to go to lake, 'f' towards forest, or 'a' to exlplore around ship: ")
    if select == "l":
        choice = "lake"
    elif select == "f":
        choice = "forest"
    elif select == "a":
        choice = "around"
    else:
        print "That was not a valid choice"
        gamestart()
"""
    Go to the lake and collect water sample.
    """
def lake():
    visitLake = """You wander towards the lake. The water looks so inviting!
    Do you seize this moment to do a cannon ball in an alien lake, or do
    you do your duty and collect a sample?
    """
    print visitLake
    select = raw_input("Press 'c' to do a cannon ball, or 's' to collect a sample.")
    if select == "s":
        global waterSamp
        if waterSamp == 1:
            print "You already have that sample, find the others!"
            gamestart()
        else:    
            print "You collect a sample with your canteen."
            global samples
            samples += 1
            print "You have %d samples" % samples
            waterSamp = 1
            global choice
            choice = samples
            gamestart()
    elif select == "c":
        print "You do a cannonball!... and something below the depths eats you!"
        global lifenumber
        lifenumber -= 1
        print " %d lives left!" % lifenumber
        gamestart()
    else:
        print "That is not a valid choice"
        lake()

""" Head to the forest to get a so
    """
def forest():
    visitForest = """
    You've decided to head to the forest. What a great opporunity to collect
    a plant specimen! Do you take this moment to explore deeper, or quickly
    collect a sample now and move on?
    """
    print visitForest  
    select = raw_input(" Press 'd' to explore deeper, or 'c' to collect right away:  ")
    if select == "d":
        global plantSamp
        if plantSamp == 1:
            print "You already have that sample, find the others!"
            gamestart()
        else:
            print "You go deeper and see the beautiful landscape, collect a few small plants, and head back to the ship."
            global samples
            samples += 1
            print "You have %d samples" % samples
            plantSamp = 1
            global choice
            choice = samples
            gamestart()
    elif select == "c":
        print "You find a nearby tangled mass of vines. You attempt to cut off a sample, and the plant comes to life and strangles you."
        global lifenumber
        lifenumber -= 1
        print " %d lives left!" % lifenumber
        gamestart()
    else:
        print "That is not a valid choice"
        forest()

def around():
    aroundShip = """
    You survey around the ship and immediately collect a jar of dirt. That was easy!"
    """
    global dirtSamp
    if dirtSamp == 1:
        print "You already have that sample, find the others!"
        gamestart()
    else:
        print aroundShip
        global samples
        samples += 1
        print "You have %d samples" % samples
        dirtSamp = 1
        global choice
        choice = samples
        gamestart()


"""
    Main Game Loop
    """
keepgoing = True
lifenumber = 3
dirtSamp = 0
waterSamp = 0
plantSamp = 0
choice = "start"
samples = 0

while keepgoing:
    print "You chose:", choice
    if choice == "start":
        gamestart()
    elif choice == "lake":
        lake()
    elif choice == "forest":
        forest()
    elif choice == "around":
        around()
