#!/usr/bin/python
import string,random,sys

# Make the random array
array = [[random.choice(string.ascii_uppercase) for i in range(10)] for j in range(10)]

# Read user file
filename = sys.argv[1]
userWords = []
with open(filename) as f:
    for line in f:
        userWords.append(line.strip('\n'))

# TODO: Check for maches
for line in array:
    line = "".join(line)
    for word in userWords:
        if word in line:
            print "found", word
