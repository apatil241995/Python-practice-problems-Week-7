class min_of_list:
  def __init__(self, lis):
    self.lis = lis

  def mim_no(self):
    
    # min is the variable holdiing the minimum value of list
    min =  self.lis[0]
    
    # checking lenth of list and calculating maximum no out of list
    if len(self.lis) > 0:
      try:
        for i in self.lis:
          if i < min:
            min = i
        return min
      except:
        return "List comtains elements of diffrent datatype"
    else:
      return "list is empty"

if __name__=="__main__":
  lis = [1,2,3,4,5]
  obj = min_of_list(lis)
  print(obj.mim_no())