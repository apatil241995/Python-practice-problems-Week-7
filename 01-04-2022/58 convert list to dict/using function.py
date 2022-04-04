list_ = ['anish','vijay','patil']
dict_ = {}

def conv_list_dict():
  global dict_
  for i in range(len(list_)):
    dict_[i] = list_[i]
  return dict_

def add_ele():
  global dict_
  dict_.update({len(dict_):"alibag"})
  return dict_

conv_list_dict()
print(add_ele())