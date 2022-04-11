# Converting Integer into string

try:
  integer =  int(input("Enter a Number: "))
  int_to_str = str(integer)
  print(integer," in string ",int_to_str," type of int_to_str ", type(int_to_str))
except:
  print("Please enter integer value")

# Converting String to integer

try:
  string = str(input("Ennter a string: "))
  str_to_int = int(string)
  print(string, " in integer ", str_to_int ," type of str_to_int ", type(str_to_int))
except:
  print("Please inter string value with base 10")


