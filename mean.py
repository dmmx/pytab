#!/usr/bin/env python

import sys

def mean(filename):
	dataset=[]
	file = open(filename, 'r')
	contents = file.readlines()

	for line in contents:
		dataset.append(int(line))

	print("Mean: " + str(sum(dataset)/len(dataset)))

if __name__ == "__main__":
	filename = sys.argv[1]
	mean(filename)
