def difference(lis):
  
  # max is the variable holdiing the maximum value of list
  max = 0
  # min is the variable holdiing the minimum value of list
  min = lis[0]
  
  # checking lenth of list and calculating maximum no out of list
  if len(lis) > 0:
    try:
      for i in lis:
          if i > max:
            max = i
          if i<min:
            min = i
      return max - min
    except:
      return "List comtains elements of diffrent datatype"
  else:
    return "list is empty"

if __name__=="__main__":
  lis = [1,2,3,4,5]
  print(difference(lis))