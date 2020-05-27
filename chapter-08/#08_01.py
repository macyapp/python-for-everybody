"""
Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
"""
def chop(t):
   del t[0]
   del t[-1]

def middle(t):
   new=t[1:]
   del new[-1]
   return new

my_list1 = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list1)
print(my_list1)                          # Should be [2,3]
print(chop_list)                        # Should be None

middle_list = middle(my_list2)
print(my_list2)                         # Should be unchanged
print(middle_list)                      # Should be [2,3]