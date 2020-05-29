"""
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""
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
