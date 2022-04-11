input_str = input("enter the string")
list = input_str.split(' ')
num_list = []
word_list= []

for i in list:
  if i.isnumeric():
    num_list.append(i)
  else:
    word_list.append(i)
      
print(num_list, word_list)
