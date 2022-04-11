lis = [1,2,3,4,5]

# max is the variable holdiing the maximum value of list
max = 0

# checking lenth of list and calculating maximum no out of list
if len(lis)>0:
  try:
    for i in lis:
      if i > max:
        max = i
  except:
    print("List comtains elements of diffrent datatype")
else:
  print("list is empty")

print(max)