from datetime import datetime
#simple way
age = 25
current_year = datetime.now().year
year_of_birth = current_year - age
no_of_leap_years = 0
lis = []
for i in range(age+1):
  year = year_of_birth
  if year % 100 != 0 and year%400 == 0:
      lis.append(year)
      year_of_birth+=1
  elif year % 4 ==0:
      lis.append(year)
      year_of_birth+=1
  else:
      year_of_birth+=1

print(lis)