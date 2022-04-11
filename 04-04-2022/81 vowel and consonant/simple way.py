lis_ = ["a","e","i","o","u","A","E","I","O","U"]
char = str(input("Enter the character: "))
if char.isalpha() and len(char)==1:
  if char in lis_:
    print("Char is vowel")
  else:
    print("Char is Consonant")
else:
  print("Please enter single alphabetic character")

