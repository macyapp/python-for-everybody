"""
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""
max=None
min=None
while True:
   num=input("Enter a number: ")
   if num=="Done" or num=="done":
      break
   try:
      num=int(num)
   except:
      print("Invalid input")
      continue
   if max is None or num>max :
      max =num
   if min is None or num < min :
      min = num
print("Max:",max,"; Min:",min)