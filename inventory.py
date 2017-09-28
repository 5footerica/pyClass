""" inventory.py
Demonstrates lists
09/19/2017 """

inventory = ["1","2","3","4","5"]

print "printing"
print inventory
print

print "now print"
print

print "then this"
print inventory[:3]
print

print "then that", inventory[3]
print

print "print again"
inventory[3] = "not 3 anymore"
print "3rd item is now: ", inventory[3]
print

print "updated inventory: "
print inventory
print

print "add to inventory: "
inventory.append("5")
print inventory
print

print "getting rid of 1"
inventory.remove("5")
print inventory
print

