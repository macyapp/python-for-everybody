"""
Suppose you are given a string and you want to count how many times each letter
appears. There are several ways you could do it:
1. You could create 26 variables, one for each letter of the alphabet. Then you
could traverse the string and, for each character, increment the corresponding
counter, probably using a chained conditional.
2. You could create a list with 26 elements. Then you could convert each
character to a number (using the built-in function ord), use the number as
an index into the list, and increment the appropriate counter.
3. You could create a dictionary with characters as keys and counters as the
corresponding values. The first time you see a character, you would add
an item to the dictionary. After that you would increment the value of an
existing item.
"""
#Normal way
word=input("Enter a word: ")
d=dict()
for c in word:
   if c not in d:
      d[c] = 1
   else:
      d[c] = d[c] + 1
print(d)