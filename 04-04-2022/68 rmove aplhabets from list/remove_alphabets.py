def remove_aphabets(lis,str_):
  if type(str_) == str and len(lis) > 0:
    for i in str_:
      if i in list_:
        list_.remove(i)
    return lis
  else:
    return "please enter string value or list is empty"

if __name__=="__main__":
  list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  str_ = str(input("enter the string: "))
  print(remove_aphabets(list_,str_))


