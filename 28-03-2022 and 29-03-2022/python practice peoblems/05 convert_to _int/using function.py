def convert_to_intiger(x):
  try:
    if type(x) == str:
      ans = int(x)
      return type(ans)
    else:
      return "Please enter a string value"
  except:
    return "Please enter a string with base value 10"

if __name__=="__main__":
  print(convert_to_intiger("10"))