""" raceAnnouncer.py
demonstrates numeric comparisons
and elif.
09/20/2017 """

for lap in range(1,11):
    print "lap", lap

    if lap == 1:
        print "Starting the race"
    elif lap < 5:
        print "still in the first half"
    elif lap == 5:
        print "halfway there..."
    elif lap == 10:
        print "Finished!"
    elif lap >= 6:
        print "getting closer"
    else:
        print "something went wrong"
    print "another great lap!"
print "That was quite a race!"
