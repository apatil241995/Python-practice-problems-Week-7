try:
  hr = int(input("Enter the no of hours: "))
  min = int(input("Enter the no of mins: "))
  if hr >= 0 and min >= 0:
    hr_in_sec = hr*60*60
    min_in_sec = min*60
  else:
    print("Please enter posetive values")
  print("Total seconds: ", hr_in_sec+min_in_sec)
except:
  print("Please enter a integer value")