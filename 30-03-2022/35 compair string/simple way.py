def comp_str(str1,str2):
  if type(str1) == str and type(str2)==str:
    if len(str1) == len(str2):
      print(str1, end='\n')
      print(str2)

    if len(str1)>len(str2):
      print(str1)
    else:
      print(str2)
  else:
    print("please enter value of string type")

if __name__=="__main__":
  comp_str("anish","anish")