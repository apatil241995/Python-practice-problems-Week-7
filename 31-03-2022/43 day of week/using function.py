from datetime import datetime

def day_of_week(date):
  a = date.split("/")
  date_of_week = datetime(int(a[0]),int(a[1]),int(a[2]))
  day_of_week = date_of_week.strftime('%A')
  return day_of_week

if __name__=="__main__":
  date = input("enter date in the format YYYY/MM/DD: ")
  day_of_week(date)
