try:
  str1 = str(input("Enter first string: "))
  str2 = str(input("enter second string: "))
  if len(str1) == len(str2):
    print(True)
  else:
    print(False)
except:
  print("Please enter values of string type")