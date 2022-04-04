tup  = (1,2,3,4,5)

def add_ele(a,ele):
  lis = list(a)
  lis.append(ele)
  return tuple(lis)

def remove_ele(a,ele):
  lis = list(a)
  lis.remove(ele)
  return tuple(lis)

def add_ele_at_index(a,index,ele):
  lis = list(a)
  lis.insert(index,ele)
  return tuple(lis)

def extend_tuple(a,b):
  lis = list(a)
  lis.extend(b)
  return tuple(lis)

  