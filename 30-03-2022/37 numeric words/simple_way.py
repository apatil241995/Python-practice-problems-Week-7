input_str = input("enter the string")
list = input_str.split(' ')
num_list = []
word_list= []

for i in list:
  for j in i:
    if j.isnumeric():
      num_list.append(j)
      a = i.replace(j,"")
      word_list.append(a)
      
print(num_list, word_list)
