try:
  a = int(input("Give a number: "))

  if a%5 == 0:
    print(True)
  else:
    print(False)
except:
  print("Please enter integer value")