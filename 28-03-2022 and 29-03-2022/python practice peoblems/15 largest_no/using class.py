class max_of_list:
  def __init__(self, Lis):
    self.Lis = Lis
  
  def max_no(self):
    # max is the variable holdiing the maximum value of list

    max = 0
    
    # checking lenth of list and calculating maximum no out of list
    if len(self.Lis) > 0:
      try:
        for i in self.Lis:
          if i > max:
            max = i
        return max
      except:
        return "List comtains elements of diffrent datatype"
    else:
      return "list is empty"

if __name__=="__main__":
  lis = [1,2,3,4,5]
  obj = max_of_list(lis)
  print(obj.max_no())