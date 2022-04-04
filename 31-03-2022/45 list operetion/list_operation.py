class List_operation:
  def __init__(self,lis):
    self.lis = lis
  
  def add_ele_last(self,ele):
    self.lis.append(ele)
    return self.lis

  def remove_ele(self,index):
    del self.lis[index]
    return self.lis
  
  def add_ele_at_index(self,index,ele):
    self.lis.insert(index,ele)
    return self.lis
