import re
suml=0
lst=[]
fhand=open("/home/sidhant/Prototype/python-for-everybody/chapter-11/regex_sum_42.txt")
for line in fhand:
   line=line.rstrip()
   x=re.findall(".+\s([0-9]+).+\s",line)
   y=re.findall(".+\S([0-9]+).+\S",line)
   x=[int(i) for i in x]
   y=[int(j) for j in y]
   lst.append(x)
   if len(x)>0:
      print(x)
