class Comp_str:
  def __init__(self,str5,str6):
    self.str5 = str5
    self.str6 = str6
  
  def ans(self):
    if type(self.str5) == str and type(self.str6):
      if len(self.str5) == len(self.str6):
        return True
      return False
    else:
      return "Please enter value of string type"

if __name__=="__main__":
  obj = Comp_str("anish","anish")
  print(obj.ans())