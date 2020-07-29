"""
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""
m=0
max=None
wor=None
f=open("mbox-short.txt")
frm=dict()
for line in f:
   line=line.rstrip()
   words=line.split()
   if len(words)<2 or words[0]!="From":
      continue
   pos=words[1].find('@')
   wor=words[1]
   wor=wor[pos+1:]
   frm[wor]=frm.get(wor,0)+1
print(frm)