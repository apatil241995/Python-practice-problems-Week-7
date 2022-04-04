#simple way 
a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd No: "))

if a%b==0:
  print(True)
else:
  print(False)

#using function 
def div_evenly(c,d):
  if c%d==0:
    return True
  return False

#using class
class Evenly_div:
  def __init__(self, e,f):
    self.e = e
    self.f = f
  
  def ans(self):
    if self.e%self.f==0:
      return True
    return False
    