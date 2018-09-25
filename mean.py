#!/usr/bin/env python

import sys

dataset=[]
filename = sys.argv[1]
file = open(filename, 'r')
contents = file.readlines()

for line in contents:
	dataset.append(int(line))

print("Mean: " + str(sum(dataset)/len(dataset)))

