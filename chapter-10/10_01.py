"""
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
fhand=open("mbox.txt")
direc=dict()
for line in fhand:
   line=line.rstrip()
   words=line.split()
   if len(words)<2 or words[0]!="From":
      continue
   wor=words[1]
   direc[wor]=direc.get(wor,0)+1

ldir=list()
for email,count in direc.items():
   ldir.append((count,email))

ldir.sort(reverse=True)

for count, email in ldir[:1]:
   print(email,count)
