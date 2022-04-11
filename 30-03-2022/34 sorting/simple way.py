#ascending sort
lis = [3,4,2,5,1,6,7,8,10]
try:
  l = len(lis)
  for i in range(l):
    for j in range(l-i-1):
      if lis[j]>lis[j+1]:
        lis[j], lis[j+1] = lis[j+1], lis[j]

  print(lis)
except:
  print("All the elements in thr list must be of same datatype")

# descending sort
lis_ = [3,4,2,5,1,6,7,8,10]
try:
  l = len(lis_)
  for i in range(l):
    for j in range(l-i-1):
      if lis_[j]<lis_[j+1]:
        lis_[j], lis_[j+1] = lis_[j+1], lis_[j]

  print(lis_)
except:
  print("All the elements in thr list must be of same datatype")
