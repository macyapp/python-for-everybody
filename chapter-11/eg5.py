# Search for lines that have an at sign between characters
# The characters must be a letter or number
import re
hand = open('/home/sidhant/Prototype/python-for-everybody/chapter-11/mbox-short.txt')
for line in hand:
   line = line.rstrip()
   x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
   if len(x) > 0:
      print(x)