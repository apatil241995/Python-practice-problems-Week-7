def ascending_sort(lis):
  l = len(lis)
  for i in range(l):
    for j in range(l-i-1):
      if lis[j]>lis[j+1]:
        lis[j], lis[j+1] = lis[j+1], lis[j]

  return lis

def descending_sort(lis_):
  l = len(lis_)
  for i in range(l):
    for j in range(l-i-1):
      if lis_[j]<lis_[j+1]:
        lis_[j], lis_[j+1] = lis_[j+1], lis_[j]
  return lis_

if __name__ == "__main__":
  lis = [3,4,2,5,1,6,7,8,10]
  lis_ = [3,4,2,5,1,6,7,8,10]
  print(ascending_sort(lis))
  print(descending_sort(lis_))