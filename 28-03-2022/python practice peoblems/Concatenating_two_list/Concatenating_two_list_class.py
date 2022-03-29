class Concatenate:
  def __init__(self,lis1,lis2):
    self.lis1 = lis1
    self.lis2 = lis2
  
  def append_lis(self):
    for i in self.lis2:
      self.lis1.append(i)
    return self.lis1

  def extend_lis(self):
    self.lis1.extend(self.lis2)
    return self.lis1
  
  def pluse_lis(self):
    return self.li1+self.lis2