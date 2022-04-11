class List_operation:
  def __init__(self,lis):
    self.lis = lis
  
  def add_ele_last(self,ele):
    self.lis.append(ele)
    return self.lis

  def remove_ele(self,ele):
    if len(self.lis)>0:
      self.lis.remove(ele)
      return self.lis
    else:
      return "list is empty"

  def add_ele_at_index(self,index,ele):
    if len(self.lis)>0:
      try:
        self.lis.insert(index,ele)
        return self.lis
      except:
        return "Index is greater than length of list please enter valid index"
    else:
      return "List is empty"

if __name__=="__main__":
  l = [1,2,3,4]
  obj = List_operation(l)
  obj.add_ele_last(5)
  obj.add_ele_at_index(3,6)
  obj.remove_ele(2)