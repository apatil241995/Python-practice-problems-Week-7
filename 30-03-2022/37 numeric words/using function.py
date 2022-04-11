def numric_word(string):
  num_list =[]
  word_list = []
  for i in string:
    if i.isnumeric():
      num_list.append(i)
    else:
      word_list.append(i)
  return f"{num_list} {word_list}"

if __name__=="__main__":
  input_str = input("enter the string")
  numric_word(input_str)