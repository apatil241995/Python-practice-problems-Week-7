def comp_str(str1,str2):
  if len(str1) == len(str2):
    print(str1, end='\n')
    print(str2)

  if len(str1)>len(str2):
    print(str1)
  else:
    print(str2)

if __name__=="__main__":
  str1 = input('Enter first string: ')
  str2 = input('Enter second string: ')
  comp_str(str1,str2)