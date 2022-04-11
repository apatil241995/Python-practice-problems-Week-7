import re
import string

def missing_letter(str1):
  if type(str1) == str:
    a = string.ascii_letters
    start = a.index(str1[0])
    stop = a.index(str1[-1])
    for i in range(start,stop,1):
      if a[i] in str1:
        continue
      else:
        return f"missing letter is {a[i]}"
  else:
    return "Please enter string value"


if __name__ == "__main__":
  b = "abdefg"
  print(missing_letter(b))