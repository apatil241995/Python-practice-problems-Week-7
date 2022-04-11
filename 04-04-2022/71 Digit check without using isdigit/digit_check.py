str_ = str(input("Enter a numeric value: "))
try:
  a = int(str_)
  print("Entered value is digit")
except:
  print("Entered value is not digit")