# simple way
lis = [1,2,3,4,5]
max = 0

for i in lis:
  if i > max:
    max = i

print(max)

# using function
def maximum(lis_):
  max_ = 0
  for i in lis_:
    if i > max_:
      max_ = i
  return max_

# using class
class max_of_list:
  def __init__(self, Lis):
    self.Lis = Lis
  
  def max_no(self):
    max = 0
    for i in self.Lis:
      if i > max:
        max = i
    return max
  
#using in built function
list = [1,2,3,4,5]
a = max(list)
print(a)