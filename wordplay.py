"""wordplay.py
demonstates turning word into list
and printing the letters
09/19/2017"""

word = "moo"
print word

print word[1]


for i in range(5):
    print i,


for i in range(2):
    print word[i],

for i in range(10,-1,-1):
    print i,

for i in range(2,-1,-1):
    print word[i]

print len(word) - 1

maxIndex = len(word) - 1

for i in range(maxIndex, -1, -1):
    print word[i],
