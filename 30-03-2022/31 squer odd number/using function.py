def squre_odd_no(lis):
  if len(lis) == 20:
    try:  
      ans = [i**2 for i in lis if i%2!=0]
      return ans
    except:
      return "Please provide list with all integer values"
  else:
    return "List is short expected list with  min length 20"

if __name__ == "__main__":
  list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  print(squre_odd_no(list_))