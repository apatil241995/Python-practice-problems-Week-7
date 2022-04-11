def remove_element(list,no_ele):
  for i in no_ele:
    try:
      #index_ is the index of element that we want to remove
      index_ = int(input("Enter the index of element to be removed: "))
      del lis[index_]
    except:
      print("Please enter a integer index_ value")
  return list

if __name__=="__main__":
  lis = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
  try:
    #no_elements holds the value of no of elements we want to remove
    no_elements = int(input("How many elements do you want to remove: "))
  except:
    print("Please enter a integer value of no_elements")
  remove_element(lis,no_elements)
