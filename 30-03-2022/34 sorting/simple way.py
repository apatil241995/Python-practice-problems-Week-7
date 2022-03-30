#ascending sort
lis = [3,4,2,5,1,6,7,8,10]
l = len(lis)
for i in range(l):
  for j in range(l-i-1):
    if lis[j]>lis[j+1]:
      lis[j], lis[j+1] = lis[j+1], lis[j]

print(lis)

# descending sort
lis_ = [3,4,2,5,1,6,7,8,10]
l = len(lis_)
for i in range(l):
  for j in range(l-i-1):
    if lis_[j]<lis_[j+1]:
      lis_[j], lis_[j+1] = lis_[j+1], lis_[j]

print(lis_)

