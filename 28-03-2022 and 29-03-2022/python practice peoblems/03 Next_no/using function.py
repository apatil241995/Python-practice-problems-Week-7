def next_no(x):
  if type(x) == int:
    return x+1
  else:
    return "Please enter a integer value"

if __name__=="__main__":
  next_no(2)