def camel_case_(str1):
  ans = ""
  if type(str1) == str:
    lis_ = str1.split(" ")
    for i in range(len(lis_)):
      if i%2 != 0:
        ans += lis_[i].capitalize()
      else:
        ans += lis_[i].lower()
    return ans
  else:
    return "Please enter a string value"

if __name__ == "__main__":
  b = "Hello world Anish patil"
  print(camel_case_(b))