from datetime import datetime

date = input("enter date in the format YYYY/MM/DD: ")
date_input = date.split("/")
date_of_the_day = datetime(int(date_input[0]),int(date_input[1]),int(date_input[2]))
day_of_week = date_of_the_day.strftime('%A')
print("Day of the week for given date: ",day_of_week)