#simple way
lis1 = [1,2,3,4,5]
if len(lis1) > 0:
  print(lis1[-1])
  print(lis1[len(lis1)-1])
else:
  print("list is empty")

#using function
def last_ele(lis2):
  return lis2[-1]

def last_ele2(lis3):
  return lis3[len(lis3)-1]

#using class
class Last_list_ele:
  def __init__(self,lis):
    self.lis = lis
  
  def ans1(self):
    return self.lis[-1]
  
  def ans2(self):
    return self.lis[len(self.lis)-1]
  