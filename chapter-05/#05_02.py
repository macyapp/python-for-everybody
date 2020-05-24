"""
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""
total=0
n=0
max=None
min=None
while True:
   num=None
   try:
      num=input("Enter a number: ")
      if num=="Done" or num=="done":
         break
      num=int(num)
      if min is None or num<min:
         min=num
      if num is None or num>max:
         max=num
      total+=num
      n+=1
   except:
      print("Invalid input")
avg=total/n
print(total,n,max,min)