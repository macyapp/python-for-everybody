#Most efficient way
word=input("Enter a word: ")
d=dict()
for c in word:
   d[c] = d.get(c,0) + 1
print(d)