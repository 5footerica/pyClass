""" ants2.py
Classic counting song
use parameters and return statements
09/20/2017 """

chorus = """
    ...and they all go marching
    down-
    to the ground-
    to get out-
    of the rain.
    Boom boom boom boom boom boom
    """
verseNum = 1

verse = """
    The ants go marching in %(verseNum)d by %(verseNum)d
    hurrah, hurrah!
    The ants go marching in %(verseNum)d by %(verseNum)d
    hurrah, hurrah!
    The ants go marching in %(verseNum)d by %(verseNum)d,
    The little one stops to %(distraction)s
        """

distraction = [
    "",
    "suck his thumb",
    "tie his shoe",
    "climb a tree"
        ]

for verseNum in range(1, len(distraction)):
    print verse(verseNum)
    print chorus()
