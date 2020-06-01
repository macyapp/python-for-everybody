"""
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""
import string
fhand=open("mbox.txt")
direc=dict()
for line in fhand:
   line=line.rstrip()
   line=line.translate(line.maketrans('', '',string.digits))
   line=line.translate(line.maketrans('','',string.punctuation))
   line=line.lower()
   words=line.split()
   if len(words)==0:
      continue
   for word in words:
      for c in word:
         direc[c]=direc.get(c,0)+1

ldir=list()
for key,value in direc.items():
   ldir.append((value,key))

ldir.sort()

for key,value in ldir:
   print(value,key)
