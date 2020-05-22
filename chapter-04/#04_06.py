"""
Exercise 6: Rewrite your pay computation with time-and-a-half for over-
time and create a function called computepay which takes two parameters
(hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

def computepay():
   try:
      hrs=float(input("Enter Hours: "))
      pay=None
      if hrs>0:
         rate=float(input("Enter Rate: "))
         if hrs>=40:
            pay=(40*rate)+((hrs-40)*1.5*rate)
         else:
            pay=hrs*rate
         print("Pay:",pay)
      else:
         print("Hours out of bounds")
   except:
      print("Error, please enter numeric input")

computepay()