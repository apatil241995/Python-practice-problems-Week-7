def numric_word(string):
  num_list =[]
  word_list = []
  for i in string:
    for j in i:
      if j.isnumeric():
        num_list.append(j)
        a = i.replace(j,"")
        word_list.append(a)
  print(num_list, end="\n")
  print(word_list)

if __name__=="__main__":
  input_str = input("enter the string")
  numric_word(input_str)