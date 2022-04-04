def remove_ele(element):
  list1 = [1,2,3,4,'anish','vijay','patil',5,6,7,8,9,10,'hii','bye','hello',11,12,13,14,15,'a','b','c','d']
  a = element
  if a.isnumeric():
    list1.remove(int(element))
  else:
    list1.remove(element)
  return list1

if __name__=="__main__":
  ele = input("Enter the element remove from list: ")
  print(remove_ele(ele))