#simple way
obj1 = 10
obj2 = 10

if obj1==obj2:
  print(True)
else:
  print(False)

#using function
def equal(obj1,obj2):
  if obj1 == obj2:
    return True
  
  return False

#using class
class compare:
  def __init__(self,obj1,obj2):
    self.obj1 = obj1
    self.obj2 = obj2
  
  def ans(self):
    if self.obj1 == self.obj2:
      return True
    return False
  
#using in built function

object1 = 10
object2 = 20

print(bool(object1==object2))
