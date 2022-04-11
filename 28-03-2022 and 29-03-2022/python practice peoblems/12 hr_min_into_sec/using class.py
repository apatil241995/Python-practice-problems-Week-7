class Hrs_mins_in_secs:
  def __init__(self,hrs,mins):
    self.hrs = hrs
    self.mins = mins
  
  def conv_hrs_in_sec(self):
    if type(self.hrs) == int:
      if self.hrs>=0:
        return self.hrs*60*60
      else:
        return "Please enter posetive no"
    else:
      return "Please enter integer value"

  
  def conv_mins_in_sec(self):
    if type(self.mins) == int:
      if self.mins>=0:
        return self.mins*60
      else:
        return "Please enter posetive no"
    else:
      return "Please enter integer value"
  
  def total_sec(self):
    hrs_in_sec = self.conv_hrs_in_sec()
    mins_in_sec = self.conv_mins_in_sec()
    return f"Total seconds {hrs_in_sec+mins_in_sec}"

if __name__=="__main__":
  obj = Hrs_mins_in_secs(10,20)
  print(obj.total_sec())