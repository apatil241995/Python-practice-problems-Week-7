from datetime import datetime
try:
  month = int(input("Enter month: "))
  year = int(input("enter year: "))
  date = datetime(year,month,13)
  day = date.strftime("%A")
  if day == "Friday":
    print(True)
  else:
    print(False)
except:
  print("Please enter a interger value for month and year")
