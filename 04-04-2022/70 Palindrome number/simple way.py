try:
  number = int(input("Enter the number"))
  if str(number)[::-1] == str(number):
    print("Number is palindome")
  else:
    print("Number is not palindome")
except:
  print("Please enter integer value")