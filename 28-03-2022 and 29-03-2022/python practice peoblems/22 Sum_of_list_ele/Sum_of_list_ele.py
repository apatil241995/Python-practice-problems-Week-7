# simple way 

lis1 = [1,2,3,4,5]
sum = 0

for i in lis1:
  sum += i

print(sum)

#using function
def Addition(lis2):
  sum1 = 0
  for i in lis2:
    sum1 += i
  return sum1

# using class
class List_sum:
  def __init__(self,lis3):
    self.lis3 = lis3
  
  def ans(self):
    sum2 = 0
    for i in self.lis3:
      sum2 += i
    return sum2
  
#using sum function
lis4 = [1,2,3,4]
print(sum(lis4))
