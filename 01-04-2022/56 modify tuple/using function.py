def add_ele(a,ele):
  lis = list(a)
  lis.append(ele)
  return tuple(lis)

def remove_ele(a,ele):
  try:
    lis = list(a)
    lis.remove(ele)
    return tuple(lis)
  except:
    return "Element not present in tuple"

def add_ele_at_index(a,index,ele):
  try:
    lis = list(a)
    lis.insert(index,ele)
    return tuple(lis)
  except:
    return "Please enter valid index"

def extend_tuple(a,b):
  lis = list(a)
  lis.extend(b)
  return tuple(lis)

if __name__=="__main__":
  tup  = (1,2,3,4,5)
  add_ele(6)
  remove_ele(2)
  add_ele_at_index(3,7)
  extend_tuple([10,9,8])