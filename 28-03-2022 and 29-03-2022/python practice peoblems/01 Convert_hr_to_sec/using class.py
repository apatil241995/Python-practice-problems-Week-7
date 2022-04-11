class Converter:
  def __init__(self, hr):
      self.hours = hr
  
  def Conv_hr_to_sec(self):
    self.sec = self.hours*60*60
    return self.sec