#simple way
a = int(input("Give a number: "))

if a%5 == 0:
  print(True)
else:
  print(False)

#using function
def check_divisibility(b):
  if b%5 == 0:
    return True
  return False

#using class
class Divisible_by5:
  def __init__(self,c):
    self.c = c

  def ans(self):
    if self.c%5 == 0:
      return True
    return False
