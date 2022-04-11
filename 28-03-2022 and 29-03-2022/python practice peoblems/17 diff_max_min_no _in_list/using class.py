class Max_Min_diff:
  def __init__(self,lis_):
    self.lis_ = lis_
  
  def diff(self):
    # max is the variable holdiing the maximum value of list
    max = 0
    # min is the variable holdiing the minimum value of list
    min = self.lis_[0]
    # checking lenth of list and calculating maximum no out of list
    if len(self.lis_) > 0:
      try:
        for i in self.lis_:
          if i > max:
            max = i
          if i < min:
            min = i
        return max - min
      except:
        return "List comtains elements of diffrent datatype"
    else:
      return "list is empty"

if __name__=="__main__":
  lis = [1,2,3,4,5]
  obj = Max_Min_diff(lis)
  print(obj.diff())