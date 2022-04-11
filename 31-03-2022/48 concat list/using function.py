def concat_list(list1,list2):
  ans = " "
  if len(list1) == len(list2):
    for i in range(len(list1)):
      ans += (f'{list1[i]+list2[i]} ')

  return ans

if __name__=="__main__":
  lis1 = ["M", "na", "i", "Ke"]
  lis2 = ["y", "me", "s", "lly"]
  concat_list(lis1,lis2)