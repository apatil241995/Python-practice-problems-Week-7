class Math_operatio:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  
  def addition(self):
    if type(self.a) == int and type(self.b) == int:
      return self.a+self.b
    else:
      return "Please enter integer value"
  
  def subtraction(self):
    if type(self.a) == int and type(self.b) == int:
      return self.a-self.b
    else:
      return "Please enter integer value"
  
  def multiplication(self):
    if type(self.a) == int and type(self.b) == int:
      return self.a*self.b
    else:
      return "Please enter integer value"
  
  def division(self):
    if type(self.a) == int and type(self.b) == int:
      return self.a/self.b
    else:
      return "Please enter integer value"
    
  
  def modulus(self):
    if type(self.a) == int and type(self.b) == int:
      return self.a%self.b
    else:
      return "Please enter integer value"
  
  def floor_division(self):
    if type(self.a) == int and type(self.b) == int:
      return self.a//self.b
    else:
      return "Please enter integer value"