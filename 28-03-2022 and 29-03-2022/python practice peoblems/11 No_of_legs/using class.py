class No_of_legson_farm:
  def __init__(self, chickens,cows,pigs):
    self.chickens = chickens
    self.cows = cows
    self.pigs = pigs
  
  def total_ans(self):
    if type(self.chickens) == int and type(self.cows)==int and type(self.pigs)==int:
      if self.chickens>=0 and self.cows>=0 and self.pigs>=0:
        total_legs = (self.chickens*2)+(self.cows*4)+(self.pigs*4)
        return total_legs
      else:
        return "Please enter posetive values"
    else:
      return "Please enter integer values"

if __name__=="__main__":
  obj = No_of_legson_farm(2,3,4)
  print(obj.total_ans())