def comp_lenth(str3,str4):
  if type(str3) == str and type(str4) == str:
    if len(str3) == len(str4):
      return True
    return False
  return "Enter values of string type"

if __name__=="__main__":
  print(comp_lenth("anish","anish"))