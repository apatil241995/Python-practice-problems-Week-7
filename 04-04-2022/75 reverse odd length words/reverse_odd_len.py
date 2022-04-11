def reverse(str1):
  if type(str1) == str:
    ans = ""
    lis = str1.split(" ")
    for i in lis:
      if len(i)%2!=0:
        a = i[::-1]
        ans += " " + a
      else:
        ans += " " + i
    return ans
  else:
    return "Please enter a string value"

if __name__ == "__main__":
  str_in = "anish vijay patil is in alibag"
  print(reverse(str_in))