lis1 = [1,2,3,4,5]

""" 
printing the last element of the list after checking length of list
using two differnt ways to print the last element of list

"""
if len(lis1) > 0:
  # method 1
  print(lis1[-1])
  #method 2
  print(lis1[len(lis1)-1])
else:
  print("list is empty")