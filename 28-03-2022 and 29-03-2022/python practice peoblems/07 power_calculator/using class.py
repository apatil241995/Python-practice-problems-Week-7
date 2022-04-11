class Power_of:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def ans_of(self):
    if type(self.a)==int and type(self.b)==int:
      answer  = self.a**self.b
      return answer
    else:
      return "Please enter integer value"

if __name__=="__main__":
  obj = Power_of(2,3)
  print(obj.ans_of())