list = ['anish','vijay','patil']
dict_ = {}

for i in range(len(list)):
  dict_[i] = list[i]

dict_.update({len(dict_): "alibag" })

print(dict_)