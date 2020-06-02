# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
hand = open('/home/sidhant/Prototype/python-for-everybody/chapter-11/mbox-short.txt')
for line in hand:
   line = line.rstrip()
   if re.search('^X\S+C.+: [0-9.]+', line):
      print(line)