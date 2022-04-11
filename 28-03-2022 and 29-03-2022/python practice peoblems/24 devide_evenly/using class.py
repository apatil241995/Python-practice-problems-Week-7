class Evenly_div:
  def __init__(self, e,f):
    self.e = e
    self.f = f
  
  def ans(self):
    if type(self.e) == int and type(self.f) == int:  
      if self.e%self.f==0:
        return True
      return False
    else:
      return "Please enter value of integer type"
  
if __name__=="__main__":
  obj = Evenly_div(4,2)
  print(obj.ans())
    