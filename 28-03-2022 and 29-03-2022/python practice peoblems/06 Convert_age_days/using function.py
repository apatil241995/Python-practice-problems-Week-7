from datetime import datetime

def age_in_days(age):
  if type(age) == int:
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

      return age_in_days
    else:
      return "Please enter positive age value"
  else:
    return "Please enter a integer value"

if __name__=="__main__":
  print(age_in_days(25))