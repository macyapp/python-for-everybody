import re
hand = open('/home/sidhant/Prototype/python-for-everybody/chapter-11/mbox-short.txt')
for line in hand:
   line = line.rstrip()
   x = re.findall('^X\S*: ([0-9.]+)', line)
   if len(x) > 0:
      print(x)