try:
  start = int(input('Give starting no: '))
  stop = int(input('give stoping no: '))
  ans = ""
  for i in range(start,stop,1):
    if i%7==0 and i%5!=0:
      ans += f"{i},"
  print(ans)
except:
  print("Please enter integer values")

