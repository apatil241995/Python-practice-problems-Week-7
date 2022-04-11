def minimum(lis):
  
  # min is the variable holdiing the minimum value of list
  min_ = lis[0]
  
  # checking lenth of list and calculating maximum no out of list
  if len(lis) > 0:
    try:
      for i in lis:
        if i < min_:
          min_=1
      return min
    except:
      return "List comtains elements of diffrent datatype"
  else:
    return "List is empty"

if __name__=="__main__":
  lis = [1,2,3,4,5]
  print(minimum(lis))