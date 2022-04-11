def lcm_(a,b):
  if type(a) == int and type(b) == int:
    if a > 0 and b > 0:
      if a > b:
        z = a
      else:
        z = b
      while(True):
        if z%a == 0 and z%b == 0:
          lcm = z
          break
        z += 1
      return f"the lcm is {lcm}"
    else:
      return "Enter a non zero value"
  else:
    return "Please enter integer value of a and b"

if __name__=="__main__":
  print(lcm_(54,24))