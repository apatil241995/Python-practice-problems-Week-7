#tacking 
input_str = input("Enter the string: ")
if "," in input_str:
  list_ = input_str.split(',')

  sorted_list = sorted(list_)

  sorted_str = ",".join(sorted_list)

  print(sorted_str)
else:
  print("enter the inputs sapereted by , ")
