import sys
import re

f1 = open(sys.argv[1],"r")
count=0
compare= re.compile('\S')
for line in f1:
	for character in line:
		if re.match(compare,character):
			count+=1
print count
