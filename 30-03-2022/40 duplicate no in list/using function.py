def duplicate_elemets(lis):
  dict = {}
  dup_ele = []
  for i in lis:
    if dict.get(i):
      dict[i] += 1
    else:
      dict[i] = 1
  
  for k,v in dict.items():
    if v > 1:
      dup_ele.append(k)
  
  return dup_ele

if __name__ == "__main__":
  lis = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1,12,88,7,6,2]
  print('list of duplecate number: ', duplicate_elemets(lis))