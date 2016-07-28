"""
This code is totally wrong. I mean including the logic.
So far in my attempts, at least logic was right.

The problem is ... while the actual number of results must be 165 numbers
based on the current text file I am using, this code prints a list of only 50 values.

That means, the placing of `mylist = []` is definitely wrong.
As a result of this mistake, the code is appending only answers to the last line 
in the text file only, leaving the remaining preceding lines.

Wrong. Totally wrong!!
"""

#!/usr/bin/python

from sys import argv

script, filename = argv

f = open(filename)
lines = f.readlines()

for line in lines:
    X, Y, N = [int(n) for n in line.split()]
    mylist = []
    for n in xrange(1, N+1):
        if n % X == 0:
                mylist.append('F')
        elif n % Y == 0:
                mylist.append('B')
        elif n % X == 0 and n & Y == 0:
                mylist.append('FB')
        else:
                mylist.append(n)

print mylist
