def remove_element(list,remove_ele_list):
  for i in remove_ele_list:
    del list[i]
  return list

if __name__=="__main__":
  lis = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
  remove_ele = [0,4,5]
  remove_element(lis,remove_ele)
