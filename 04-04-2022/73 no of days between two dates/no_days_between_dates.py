def no_of_days(date1,date2):
  month_days = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
  leapyear_month_days = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
  no_of_years = date1[0]-date2[0]
  print(no_of_years)
  no_of_leapyears = 0
  for i in range(date1[0],date2[0],1):
    if i%400 == 0 and i%100 != 0:
      no_of_leapyears += 1
    elif i%4 == 0:
      no_of_leapyears += 1
  non_leapyears = no_of_years-no_of_leapyears