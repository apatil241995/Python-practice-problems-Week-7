def hrs_in_secs(hrs):
  if type(hrs) == int:
    if hrs>=0:
      return hrs*60*60
    else:
      return "Please enter posetive no"
  else:
    return "Please enter integer value"


def mins_in_secs(mins):
  if type(mins) == int:
    if mins>=0:
      return mins*60
    else:
      return "Please enter posetive no"
  else:
    return "Please enter integer value"

def total_sec(hr,mi_n):
  hr_in_sec = hrs_in_secs(hr)
  min_in_sec = mins_in_secs(mi_n)
  return "total seconds", hr_in_sec+min_in_sec

if __name__=="__main__":
  print(total_sec(10,20))