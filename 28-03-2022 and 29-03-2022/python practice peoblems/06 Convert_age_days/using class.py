from datetime import datetime

class Agein_days:
  def __init__(self, age):
    self.age = age

  def calc_age_in_days(self):
    if type(self.age) == int:
      if self.age > 0:
        #checking the current year
        current_year = datetime.now().year
        #calculating year of birth by subtracting age from current year
        year_of_birth = current_year - self.age
        #holds the no of leap years from year or birth to current year
        no_of_leap_years = 0
        #calculating no of leap years
        for i in range(self.age+1):
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
        age_in_days = ((self.age-no_of_leap_years)*365)+(no_of_leap_years*366)

        return age_in_days
      else:
        return "Please enter a positive age vlaue"
    else:
      return "Please enter a integer value"