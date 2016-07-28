#!/usr/bin/python

from sys import argv

script, filename = argv

f = open(filename)
lines = f.readlines()

for line in lines:
    X, Y, N = [int(n) for n in line.split()]

    for n in xrange(1, N+1):
        if n % X == 0:
                print 'F'
        elif n % Y == 0:
                print 'B'
        elif n % X == 0 and n & Y == 0:
                print 'FB'
        else:
                print n
