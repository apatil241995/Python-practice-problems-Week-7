lis = [1,2,3,4,5]

# min is the variable holdiing the minimum value of list
min = lis[0]

# checking lenth of list and calculating maximum no out of list
if len(lis)>0:
  try:
    for i in lis:
      if i<min:
        min = i
  except:
    print("List comtains elements of diffrent datatype")
else:
  print("list is empty")

print(min)