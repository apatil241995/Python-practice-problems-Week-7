from operator import le


class List_sum:
  def __init__(self,lis3):
    self.lis3 = lis3
  
  def ans(self):
    sum2 = 0
    if len(self.lis3):
      for i in self.lis3:
        sum2 += i
      return sum2
    else:
      return "list is empty"

if __name__=="__main__":
  lis1 = [1,2,3,4,5]
  obj = List_sum(lis1)
  print(obj.ans())