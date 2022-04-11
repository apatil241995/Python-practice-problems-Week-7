def nigative_sum(str_):
  sum_ = 0
  lis = str_.split(" ")
  for i in range(len(lis)-1):
    if lis[i] == "-":
      if lis[i+1].isnumeric():
        sum_+= -(int(lis[i+1]))
  return sum_

if __name__=="__main__":
  str_ = "22 13 % 14 & - 11 - 22 13 12"
  print(nigative_sum(str_))
