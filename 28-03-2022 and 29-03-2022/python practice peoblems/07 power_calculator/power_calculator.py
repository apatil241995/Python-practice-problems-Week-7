# simple way
a = 2
b = 3

ans = a**b
print(ans)

# using function
def power(a,b):
  return a**b

# using class
class Power_of:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def ans_of(self):
    answer  = self.a**self.b
    return answer

# using library
c = 2
d = 3

z = pow(c,d)
print(z)
