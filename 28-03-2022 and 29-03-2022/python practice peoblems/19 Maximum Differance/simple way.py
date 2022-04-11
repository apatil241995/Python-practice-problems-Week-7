list = [2,1,3,4,5]
# max is the variable holdiing the maximum value of list
max = 0
# min is the variable holdiing the minimum value of list
min = list[0]

# checking lenth of list and calculating maximum no out of list
if len(list)>0:
  try:
    for i in list:
      if i > max:
        max = i
      if i < min:
        min = i
  except:
    print("List comtains elements of diffrent datatype")
else:
  print("list is empty")

print("Differance of max and min no in list: ",max-min)
