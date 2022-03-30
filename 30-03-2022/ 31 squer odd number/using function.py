def squre_odd_no(lis):
  ans = [i**2 for i in lis if i%2!=0]
  return ans

if __name__ == "__main__":
  list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  print(squre_odd_no(list_))