def even_digits(start,stop):
  count = 0
  list_ = []
  if start>0 and stop>0 and start!=stop:
    for i in range(start,stop,1):
      a = str(i)
      for j in a:
        if int(j)%2==0:
          count += 1
      if count == len(a):
        count = 0
        list_.append(i)
      else:
        count = 0

    ans = ','.join(list_)
    return ans
  else:
    return "Enter Posetive value"

if __name__ == "__main__":
  try:
    start_ = int(input("Enter the starting no: "))
    stop_ = int(input("Enter the stoping no:"))
    print(even_digits(start_,stop_))
  except:
    print("Please enter integer values")