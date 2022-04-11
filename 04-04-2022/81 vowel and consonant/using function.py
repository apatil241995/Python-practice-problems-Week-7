def check_vowe_or_consonant(char):
  lis_ = ["a","e","i","o","u","A","E","I","O","U"]
  if type(char) == str:
    if char.isalpha and len(char) == 1:
      if char in lis_:
        return "Char is vowel"
      else:
        return "Char is Consonant"
    else:
      return "Enter a single alphabetic char"
  else:
    return "Enter a string value"

if __name__=="__main__":
  check_vowe_or_consonant("a")