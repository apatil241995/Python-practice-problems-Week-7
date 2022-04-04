class Modify_tuple:
  def __init__(self,tup):
    self.tup = tup
  
  def add_ele(self,ele):
    lis = list(self.tup)
    lis.append(ele)
    return tuple(lis)

  def remove_ele(self,ele):
    lis = list(self.tup)
    lis.remove(ele)
    return tuple(lis)

  def add_ele_at_index(self,index,ele):
    lis = list(self.tup)
    lis.insert(index,ele)
    return tuple(lis)

  def extend_tuple(self,b):
    lis = list(self.tup)
    lis.extend(b)
    return tuple(lis)