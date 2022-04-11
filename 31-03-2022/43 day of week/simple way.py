from datetime import datetime

#taking date as string in form of YYYY/MM/DD
date = input("enter date in the format YYYY/MM/DD: ")

#converting the date into list
date_input = date.split("/")

#Actual date of day
date_of_the_day = datetime(int(date_input[0]),int(date_input[1]),int(date_input[2]))

#getting week day using strtime function in date time module
day_of_week = date_of_the_day.strftime('%A')
print("Day of the week for given date: ",day_of_week)