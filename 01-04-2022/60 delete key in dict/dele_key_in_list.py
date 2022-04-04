dict1 = {'1':2,'3':4,'5':6}

dele_key = input("Enter the key to delete: ")
if dele_key in dict1:
  dict1.pop(dele_key)
else:
  print("No such key exists")