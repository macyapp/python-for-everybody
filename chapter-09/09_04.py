"""
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dic-
tionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
m=0
max=None
f=open("mbox.txt")
frm=dict()
for line in f:
   line=line.rstrip()
   words=line.split()
   if len(words)<2 or words[0]!="From":
      continue
   frm[words[1]]=frm.get(words[1],0)+1
for key in frm:
   if frm[key]>m:
      max=key
      m=frm[key]
print(max,m)
