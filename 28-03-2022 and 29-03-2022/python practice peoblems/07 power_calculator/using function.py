def power(a,b):
  if type(a) == int and type(b) == int:
    return a**b
  else:
    return "please enter a integer value"
  
if __name__=="__main__":
  print(power(2,3))
