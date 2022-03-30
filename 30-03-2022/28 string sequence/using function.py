def sorted_str():
  inp_str = input('Enter the string: ')
  list_ = inp_str.split(',')
  sorted_lis = sorted(list_)
  ans = ",".join(sorted_lis)
  return ans

if __name__ == "__main__":
  print(sorted_str())