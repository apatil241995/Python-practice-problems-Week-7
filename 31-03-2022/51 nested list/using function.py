def add_sub_list(ind):
  nested_list = [1,2,3,4,[5,6,7,8],9,10,[20,11,12]]
  sub_list = ["i","am","sub list"]
  nested_list.insert(ind,sub_list)
  return nested_list

if __name__=="__main__":

  index = int(input("enter the index: "))
  print(add_sub_list(index))