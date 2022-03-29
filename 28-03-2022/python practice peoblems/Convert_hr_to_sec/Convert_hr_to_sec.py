# simple way
hr = 5
sec = hr*60*60
print(sec)

# using fuction 
def conv_hr_to_sec(b):
  sec =  b *60*60
  return sec

# using Class
class Converter:
  def __init__(self, hr):
      self.hours = hr
  
  def Conv_hr_to_sec(self):
    self.sec = self.hours*60*60
    return self.sec

# using library
from datetime import timedelta
hours = timedelta(hours=5)
secs = hours.total_seconds()
print(secs)