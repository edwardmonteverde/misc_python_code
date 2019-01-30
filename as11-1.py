#cd Desktop\Coursera\Python\Class 3

import re

filename = input("Enter file: ")
if len(filename) < 1:
	filename = "regex_sum_42.txt"
if len(filename) == 1:
	filename = "regex_sum_141650.txt"

fhand = open(filename)

endlist = list()
for line in fhand:
	
	numlist = re.findall('[0-9]+', line)
	nl = len(numlist)
	if nl < 1: continue
	
	x = 0
	while x < nl:
		num = numlist[x]
		endlist.append(int(num))
		x = x + 1

print(sum(endlist))