def identical_items(set1,set2):
  identical_ele = set({})
  for i in set1:
    if i in set2:
      identical_ele.add(i)
  return identical_ele

if __name__=="__main__":
  s1 = {1,2,3,4,5}
  s2 = {1,6,7,3,8,2,9}
  print("set of identical items fron two sets is ",identical_items(s1,s2))
