class Divisible_by5:
  def __init__(self,c):
    self.c = c

  def ans(self):
    if type(self.c) == int:
      if self.c%5 == 0:
        return True
      return False
    else:
      return "Please enter integer value"