from ast import Try


def exceptions():
  try:  
    return 5/0
  except ZeroDivisionError:
    return "Can not divide a number by zero"

print(exceptions())
