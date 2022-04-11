list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
if len(list_) == 20:
  try:
    ans = [i**2 for i in list_ if i%2!=0]
    print(ans)
  except:
    print("Please provide list with all integer values")
else:
  print("List is short expected list with  min length 20")