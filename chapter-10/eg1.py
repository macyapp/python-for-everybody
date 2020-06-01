#A program to sort words in a descending word length order
txt = 'but soft what light in yonder window breaks'
words = txt.split()
print(words)

t = list()
print(t)

for word in words:
   t.append((len(word),word))

print(t)

t.sort(reverse=True)             #sort compares the first element, length, first, and only considers the second
                                 #element to break ties.
print(t)

res = list()
for length, word in t:
   res.append(word)

print(res)