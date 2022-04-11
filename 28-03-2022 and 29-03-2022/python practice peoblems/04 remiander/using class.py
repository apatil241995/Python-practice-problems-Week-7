class rem:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def ans(self):
    if type(self.a) == int and type(self.b)==int:
      return "reminder is ",self.a%self.b
    else:
      return "please enter a integer value"