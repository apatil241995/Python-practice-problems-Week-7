#simple way 
a = "2"
intiger_a = int(a)
print(intiger_a)

#using function
def convert_to_intiger(x):
  return int(x)

#using class
class ConvertTo_intiger:
  def __init__(self, strng):
      self.strng = strng
    
  def ans(self):
    return int(self.strng)
