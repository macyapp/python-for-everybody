"""
Exercise 3: Encapsulate this code in a function named count, and gen-
eralize it so that it accepts the string and the letter as arguments.
"""
def count(word,char):
   word = 'banana'
   count = 0
   for letter in word:
      if letter == char:
         count+=1
   print(count)

s=input("Enter a string: ")
c=input("Enter a character: ")
count(s,c)