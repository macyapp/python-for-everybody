"""
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
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

