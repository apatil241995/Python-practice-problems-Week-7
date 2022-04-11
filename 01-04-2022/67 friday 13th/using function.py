from datetime import datetime
def Friday_13(year,month):
  if type(year) == int and type(month) == int:
    date = datetime(year,month,13)
    day = date.strftime("%A")
    if day == "Friday":
      return True
    else:
      return False
  else:
    return "Please enter a interger value for month and year"
  
if __name__=="__main__":
  print(Friday_13(2022,2))