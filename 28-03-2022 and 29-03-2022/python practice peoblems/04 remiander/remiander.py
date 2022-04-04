#simple method
a = 13
b = 2
rem = a%b
print(rem)

#using function
def rem(a,b):
  return a%b

#using class
class rem:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def ans(self):
    return self.a%self.b

#using library
from math import remainder

c = 13
d = 2
ans = remainder(c,d)
print(ans)
      