from datetime import datetime

def day_of_week(date):
  
  #converting the date into list
  a = date.split("/")
  
  #Actual date of day
  date_of_week = datetime(int(a[0]),int(a[1]),int(a[2]))
  
  #getting week day using strtime function in date time module
  day_of_week = date_of_week.strftime('%A')
  return day_of_week

if __name__=="__main__":
  #taking date as string in form of YYYY/MM/DD
  date = input("enter date in the format YYYY/MM/DD: ")
  day_of_week(date)
