def maximum(lis_):

  # max is the variable holdiing the maximum value of list
  max_ = 0

  # checking lenth of list and calculating maximum no out of list
  if len(lis_) > 0:
    try:
      for i in lis_:
        if i > max_:
          max_ = i
      return max_
    except:
      return "List comtains elements of diffrent datatype"
  else:
    return "list is empty"

if __name__=="__main__":
  lis = [1,2,3,4,5]
  print(maximum(lis))