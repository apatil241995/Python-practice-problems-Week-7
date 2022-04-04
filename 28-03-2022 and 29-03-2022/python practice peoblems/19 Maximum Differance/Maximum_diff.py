#simple way

list = [2,1,3,4,5]
max = 0
min = list[0]

for i in list:
  if i > max:
    max = i
  if i < min:
    min = i

print("Differance of max and min no in list: ",max-min)

#using function
def difference(lis):
  max = 0
  min = lis[0]

  for i in lis:
    if i > max:
      max = i
    if i<min:
      min = i
  
  return max - min

#using class
class Max_Min_diff:
  def __init__(self,lis_):
    self.lis_ = lis_
  
  def diff(self):
    max = 0
    min = self.lis_[0]
    for i in self.lis_:
      if i > max:
        max = i
      if i < min:
        min = i
    return max - min

#using in built function
list_ = [1,2,3,4,5]
max_ = max(list_)
min_ = min(list_)

print('Difference between max and min no in list is: ', max_ - min_)