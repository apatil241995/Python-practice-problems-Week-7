class Next_no:
  def __init__(self, x):
    self.x = x
  
  def ans(self):
    if type(self.x) == int:
      return self.x+1  
    else:
      return "Please enter a integer value"