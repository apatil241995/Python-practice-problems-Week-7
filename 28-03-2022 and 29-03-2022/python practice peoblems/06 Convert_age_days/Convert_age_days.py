from datetime import datetime
#simple way
age = 25
current_year = datetime.now().year
year_of_birth = current_year - age
no_of_leap_years = 0
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

age_in_days = ((age-no_of_leap_years)*365)+(no_of_leap_years*366)

print(age_in_days)

#using function
def age_in_days(age):
  current_year = datetime.now().year
  year_of_birth = current_year - age
  no_of_leap_years = 0
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

  age_in_days = ((age-no_of_leap_years)*365)+(no_of_leap_years*366)

  return age_in_days

b = age_in_days(25)
print(b)

#using class
class Agein_days:
  def __init__(self, age):
    self.age = age

  def calc_age_in_days(self):
    current_year = datetime.now().year
    year_of_birth = current_year - self.age
    no_of_leap_years = 0
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

    age_in_days = ((self.age-no_of_leap_years)*365)+(no_of_leap_years*366)

    return age_in_days