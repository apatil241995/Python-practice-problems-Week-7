try:
  a = int(input("Enter 1st no: "))
  b = int(input("Enter 2nd No: "))

  if a%b==0:
    print(True)
  else:
    print(False)
except:
  print("Please enter value of integer type")