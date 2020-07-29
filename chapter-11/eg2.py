import re
hand = open('mbox.txt')
for line in hand:
   line = line.rstrip()
   if re.search('^F..m:', line):
      print(line)