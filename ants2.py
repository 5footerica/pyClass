""" ants2.py
Classic counting song
use parameters and return statements
09/20/2017 """

def chorus():
    output = """
    ...and they all go marching
    down-
    to the ground-
    to get out-
    of the rain.
    Boom boom boom boom boom boom
    """
    return output

def versus(verseNum):
    if verseNum == 1:
        distraction = "suck his thumb"
    elif verseNum == 2:
        distraction = "tie his shoe"
    else:
        distraction = "I have no idea"

    output = """
    The ants go marching in %(verseNum)d by %(verseNum)d
    hurrah, hurrah!
    The ants go marching in %(verseNum)d by %(verseNum)d
    hurrah, hurrah!
    The ants go marching in %(verseNum)d by %(verseNum)d,
    The little one stops to %(distraction)s
        """ % vars()
    return output
        

print versus(1)
print chorus()
print versus(2)
print chorus()
