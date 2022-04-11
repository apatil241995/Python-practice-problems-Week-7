try:
  hr = int(input("Enter no of hours: "))
  sec = hr*60*60
  print(sec)
except:
  print("Please enter a integer value")