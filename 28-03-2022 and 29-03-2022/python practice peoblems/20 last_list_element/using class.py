""" 
created class to print the last element of the list after checking length of list
using two differnt ways to print the last element of list

"""
class Last_list_ele:
  def __init__(self,lis):
    self.lis = lis
  
  #method 1
  def ans1(self):
    if len(self.lis) > 0:
      return self.lis[-1]
    else:
      return "list is empty" 
  
  #method 2
  def ans2(self):
    if len(self.lis)>0:
      return self.lis[len(self.lis)-1]
    else:
      return "list is empty"