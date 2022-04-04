try:
  no = int(input("Enter the no: "))
  str_no = str(no)
  length = 0
  for i in str_no:
    length += 1
  print(f"lenght of {no} is: ",length)
except:
  print("Please enter a integer value")