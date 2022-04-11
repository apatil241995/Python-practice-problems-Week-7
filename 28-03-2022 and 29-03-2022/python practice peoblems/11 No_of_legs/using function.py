def no_of_legs(chickens,cows,pigs):
  if type(chickens) == int and type(cows)==int and type(pigs)==int:
    if chickens>=0 and cows>=0 and pigs>=0:
      total_legs = (chickens*2)+(cows*4)+(pigs*4)
      return total_legs
    else:
      return "Please enter posetive values"
  else:
    return "Please enter integer values"

if __name__=="__main__":
  print(no_of_legs(2,4,5))