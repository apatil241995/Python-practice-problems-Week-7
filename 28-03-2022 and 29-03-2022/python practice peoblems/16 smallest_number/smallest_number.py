#simple way
lis = [1,2,3,4,5]
min = lis[0]

for i in lis:
  if i<min:
    min = i

print(min)

#using function
def minimum(LIS):
  min_ = LIS[0]
  for i in LIS:
    if i < min_:
      min_=1
  return min

#using class
class min_of_list:
  def __init__(self, lis):
    self.lis = lis

  def mim_no(self):
    min =  self.lis[0]
    for i in self.lis:
      if i < min:
        min = i
    return i
  
  #using in built function
  lis_ = [1,2,3,4,5]
  a = min(lis_)
  print(a)