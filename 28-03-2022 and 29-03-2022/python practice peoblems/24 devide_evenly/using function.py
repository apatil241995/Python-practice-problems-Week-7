def div_evenly(c,d):
  if type(c) == int and type(d) == int:
    if c%d==0:
      return True
    return False
  else:
    return "Please enter value of integer type"

if __name__=="__mian__":
  print(div_evenly(4,2))