"""
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.

Score Grade
>=0.9 A
>=0.8 B
>=0.7 C
>=0.6 D
<0.6  F
"""
def computegrade():
   while True:
      score=None
      try:
         score=input("Enter score:")
         if score=="done" or score=="done":
            print("Done!")
            break
         score=float(score)
         if score>=0 and score<=1:
            if score>=0.9:
               print('A')
            elif score>=0.8:
               print('B')
            elif score>=0.7:
               print('C')
            elif score>=0.6:
               print('D')
            else:
               print('F')
         else:
            print("Score out of bounds!")
      except:
         print("Bad score")

computegrade()
