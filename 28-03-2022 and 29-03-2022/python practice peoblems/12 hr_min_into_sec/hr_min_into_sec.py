#simple way
hr = 10
min = 20

hr_in_sec = hr*60*60
min_in_sec = min*60

print("Hours in seconds: ", hr_in_sec)
print("Minutes in seconds: ", min_in_sec)

#using function
def hrs_in_secs(hrs):
  return hrs*60*60

def mins_in_secs(mins):
  return mins*60

#using class
class Hrs_mins_in_secs:
  def __init__(self,hrs,mins):
    self.hrs = hrs
    self.mins = mins
  
  def conv_hrs_in_sec(self):
    return self.hrs*60*60
  
  def conv_mins_in_sec(self):
    return self.mins*60
 
#using library
from datetime import timedelta

hrs = timedelta(hours=10)
mins = timedelta(minutes=10)
hrs_in_sec = hrs.total_seconds()
mins_in_sec = mins.total_seconds()

print("Hours in sec using datetime: ",hrs_in_sec)
print("Minutes in sec using datetime: ",min_in_sec)