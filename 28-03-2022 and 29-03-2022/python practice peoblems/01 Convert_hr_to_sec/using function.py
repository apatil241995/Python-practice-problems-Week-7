def conv_hr_to_sec(b):
  if type(b)==int:
    sec =  b *60*60
    return sec
  else:
    return "Please enter a integer value"