def occ_ele(lis):

  #using dict to store element as key and it's occurance as value
  dict = {}
  for i in lis:
    if dict.get(i):
      dict[i] += 1
    else:
      dict[i] = 1
  return dict


if __name__=="__main__":
  sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
  print(occ_ele(sample_list))