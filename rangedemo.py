""" rangedemo.py
demonstrates how range object
creates automatic lists of #'s
09/19/2017"""

print "range(3)"
print range(3)
print

print "range(1, 3)"
print range(1,3)
print

print "range(2,5)"
print range(2,5)
print

print "range(0,55,5)"
print range(0,55,5)
print

print "range(50,0,-5)"
print range(50,0,-5)
print

for i in range(10):
    print "burp"

for lap in range(1,11):
    print "burp", lap

for merp in range(55,0,-5):
    print "burp", merp
