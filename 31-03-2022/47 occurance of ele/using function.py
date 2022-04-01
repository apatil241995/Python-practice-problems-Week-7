def occ_ele(lis):
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