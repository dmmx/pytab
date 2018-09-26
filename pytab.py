#!/usr/bin/env python

import sys
from mean import mean
from median import median

filename = "(null)"
if len(sys.argv) == 2:
	filename = sys.argv[1]

command =""
while command != "exit":
	command = input("ptb > ")
	if command == "filename":
		print(filename)
	elif command == "mean":
		mean(filename)
	elif command == "median":
		median(filename)
	elif command == "exit":
		pass
	else:
		print("INVALID COMMAND")


print("That's all folks")

