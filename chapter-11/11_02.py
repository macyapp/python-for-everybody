"""
Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
"""
import re
count=0
total=0
avg=0
fname="mbox.txt"
fhand=open(fname)
inp="^New.+: ([0-9]+)"
for line in fhand:
   line=line.rstrip()
   x=re.findall(inp,line)
   x=[int(i) for i in x]
   for i in x:
      total+=i
      count+=1
avg=total//count
print(avg)
