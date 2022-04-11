def ascending_sort(lis):
  try:
    l = len(lis)
    for i in range(l):
      for j in range(l-i-1):
        if lis[j]>lis[j+1]:
          lis[j], lis[j+1] = lis[j+1], lis[j]

    return lis
  except:
    return "All the elements in thr list must be of same datatype"

def descending_sort(lis_):
  try:
    l = len(lis_)
    for i in range(l):
      for j in range(l-i-1):
        if lis_[j]<lis_[j+1]:
          lis_[j], lis_[j+1] = lis_[j+1], lis_[j]
    return lis_
  except:
    return "All the elements in thr list must be of same datatype"
    
if __name__ == "__main__":
  lis = [3,4,2,5,1,6,7,8,10]
  lis_ = [3,4,2,5,1,6,7,8,10]
  print(ascending_sort(lis))
  print(descending_sort(lis_))