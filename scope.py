""" scope.py
illustrates scope and functions
09/20/2017 """

varOutside = "I was created outside the function"
print "outside the function, varOutside is: %s" % varOutside

def theFunction():
    varInside = "I was made inside the function"
    print "inside the function, varOutside is: %s" % varOutside
    print "inside the function , varInside is: %s" % varInside

theFunction()

print "back outside the function, varOutside is: %s" % varOutside
# if I uncommment the next line, the program will crash
#print "back outside the function, varInside is %s" % varInside
