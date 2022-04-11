from datetime import datetime
try:
  age = int(input("Enter the age: "))
  if age > 0:
    #checking the current year
    current_year = datetime.now().year
    #calculating year of birth by subtracting age from current year
    year_of_birth = current_year - age
    #holds the no of leap years from year or birth to current year
    no_of_leap_years = 0
    #calculating no of leap years
    for i in range(age+1):
      a = year_of_birth
      if a%100 != 0 and a%400 == 0:
        no_of_leap_years += 1
        year_of_birth += 1
      elif a%4 == 0:
        no_of_leap_years += 1
        year_of_birth += 1
      else:
        year_of_birth += 1

    #calculating age in days
    age_in_days = ((age-no_of_leap_years)*365)+(no_of_leap_years*366)

    print(age_in_days)
  else:
    print("Please enter a positve age value")
except:
  print("Please enter a intiger value")