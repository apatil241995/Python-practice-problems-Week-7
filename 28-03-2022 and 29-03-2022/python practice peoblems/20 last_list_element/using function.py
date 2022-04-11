""" 
created two fuctions to print the last element of the list after checking length of list
using two differnt ways to print the last element of list

"""
#method 1
def last_ele(lis2):
  if len(lis2) > 0:
    return lis2[-1]
  else:
    return "list is empty"

# method 2
def last_ele2(lis3):
  if len(lis3) > 0:
    return lis3[len(lis3)-1]
  else:
    return "list is empty"

if __name__=="__main__":
  lis1 = [1,2,3,4,5]
  print(last_ele(lis1))
  print(last_ele2(lis1))