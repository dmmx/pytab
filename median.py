import sys
import math

dataset=[]
filename = sys.argv[1]
file = open(filename, 'r')
contents = file.readlines()
for line in contents:
#	print(line)
	dataset.append(float(line))

#for n in dataset:
#	print(n)

dataset.sort()

if len(dataset) % 2 == 0:
	index1 = int(len(dataset)/2)
	index2 = int(len(dataset)/2+1)
	print("l(M):   " + str((index1+index2)/2))
#	print(str(dataset[index1]) + ", " + str(dataset[index2]))
	print("Median: " + str((dataset[index1-1]+dataset[index2-1])/2))
else:
	index = math.ceil(len(dataset)/2)
	print("l(M):   " + str(index))
	print("Median: " + str(dataset[index-1]))

