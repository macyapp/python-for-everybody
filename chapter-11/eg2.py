import re
hand = open('/home/sidhant/Prototype/python-for-everybody/chapter-11/mbox.txt')
for line in hand:
   line = line.rstrip()
   if re.search('^F..m:', line):
      print(line)