class S_um:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def Ans(self):
    if type(self.a) == type(self.b):
      return "Sum is ", self.a + self.b
    else:
      return "Please enter the value of same datatype"

if __name__=="__main__":
  obj = S_um(1,2)
  print(obj.Ans())