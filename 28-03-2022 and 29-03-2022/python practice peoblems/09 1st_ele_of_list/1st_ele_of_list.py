#Simple way
lis = [1,2,3,4,5]
print(lis[0])

#using function
def first_ele(list):
  return list[0]

#using class
class First_ele_list:
  def __init__(self, LIST):
    self.LIST = LIST
  
  def ans(self):
    return  self.LIST[0]