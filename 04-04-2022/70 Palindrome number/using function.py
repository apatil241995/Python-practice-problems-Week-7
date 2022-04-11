def palindrome_check(num):
  if type(num) == int:
    if str(num)[::-1] == str(num):
      return "Number is palindrome"
    else:
      return "Number is not palindrome"
  else:
    return "Please enter as integer value as number"
  
if __name__=="__main__":
  print(palindrome_check(111))