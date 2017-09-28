""" password.py
Ask the user for a password
repeat until user gets it right
or has tried 3 times
09/20/2017 """

keepGoing = True
correct = "Python"
tries = 3

while keepGoing:
    guess = raw_input("Please enter the password: ")
    tries = tries - 1

    if guess == correct:
        print "You may proceed"
        keepGoing = False

    else:
        print "That's not correct."

        if tries <= 0:
            print "Sorry, you only had 3 tries"
            keepGoing = False
        else:
            print "You have %d tries left" % tries
