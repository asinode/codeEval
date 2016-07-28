#!/usr/bin/python

import sys

with open(sys.argv[1], 'r') as file:
	lines = file.read().strip().splitlines()

for line in lines:
    X, Y, N = (int(n) for n in line.split())
    all_fs = {X * i for i in xrange(1, N+1)}
    all_bs = {Y * i for i in xrange(1, N+1)}

    for n in xrange(1, N+1):
	if n in all_fs and n in all_bs:
		print 'FB'
	elif n in all_fs:
		print 'F'
	elif n in all_bs:
		print 'B'
	else:
		print n
    print
