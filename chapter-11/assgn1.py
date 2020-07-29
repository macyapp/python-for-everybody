import re
suml=0
fhand=open("regex_sum_537045.txt")
for line in fhand:
   line=line.rstrip()
   x=re.findall("([0-9]+)",line)
   x=[int(i) for i in x]
   for i in x:
      suml+=i
   #if len(x)>0:
   #   print(x)
print(suml)
