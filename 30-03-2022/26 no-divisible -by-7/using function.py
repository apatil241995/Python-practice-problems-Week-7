def sequence(start,stop):
  ans = ""
  for i in range(start,stop,1):
    if i%7==0 and i%5!=0:
      ans += f"{i},"
  return ans

if __name__ == "__main__":
  try:
    start = int(input('Give starting no: '))
    stop = int(input('give stoping no: '))
    print(sequence(start,stop))
  except:
    print("Please enter integer values")