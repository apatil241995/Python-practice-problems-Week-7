def length_of_no(no):
  length = 0
  if type(no) == int:
    str_no = str(no)
    for i in str_no:
      length += 1
    return length
  else:
    return "Please enter a intiger"

if __name__=="__main__":
  try:
    n =  int(input("enter the no: "))
    print(length_of_no(n))
  except:
    print("Please enter a valide integer")
