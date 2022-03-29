#simple method
a = 10
next_no = a+1
print(next_no)

#using function
def next_no(x):
  return x+1

#using class
class Next_no:
  def __init__(self, x):
    self.x = x
  
  def ans(self):
    return self.x+1      