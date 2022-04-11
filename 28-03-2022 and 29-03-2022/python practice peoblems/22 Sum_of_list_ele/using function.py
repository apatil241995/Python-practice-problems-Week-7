def Addition(lis2):
  sum1 = 0
  if len(lis2)>0:
    for i in lis2:
      sum1 += i
    return sum1
  else:
    return "list is empty"

if __name__=="__main__":
  lis1 = [1,2,3,4,5]
  print(Addition(lis1))