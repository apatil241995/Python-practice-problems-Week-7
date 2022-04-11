def rem(a,b):
  if type(a) == int and type(b)==int:
    return "reminder is ",a%b
  else:
    return "please enter a integer value"


print(rem(3,2))