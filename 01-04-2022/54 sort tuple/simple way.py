tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

lis = list(tuple1)
l = len(lis)

#ascending order
for i in range(l):
  for j in range(l-i-1):
    if lis[j][1] > lis[j+1][1]:
      lis[j],lis[j+1] = lis[j+1],lis[j]

print(tuple(lis))

#decending order
for i in range(l):
  for j in range(l-i-1):
    if lis[j][1] < lis[j+1][1]:
      lis[j],lis[j+1] = lis[j+1],lis[j]

print(tuple(lis))
