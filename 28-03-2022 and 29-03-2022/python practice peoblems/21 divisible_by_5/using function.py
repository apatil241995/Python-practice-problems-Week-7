def check_divisibility(b):
  if type(b) == int:
    if b%5 == 0:
      return True
    return False
  else:
    return "Please enter integer value"

if __name__=="__main__":
  print(check_divisibility(5))