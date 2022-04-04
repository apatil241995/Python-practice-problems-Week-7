def ascending(tup):
  lis = list(tup)
  l = len(lis)
  for i in range(l):
    for j in range(l-i-1):
      if lis[j][1] > lis[j+1][1]:
        lis[j],lis[j+1] = lis[j+1],lis[j]
  return tuple(lis)

def descending(tup):
  lis = list(tup)
  l = len(lis)
  for i in range(l):
    for j in range(l-i-1):
      if lis[j][1] < lis[j+1][1]:
        lis[j],lis[j+1] = lis[j+1],lis[j]
  return tuple(lis)

if __name__=="__main__":
  tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
  print(ascending(tuple1))
  print(descending(tuple1))