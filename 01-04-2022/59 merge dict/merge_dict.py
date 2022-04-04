dict1 = {1:2,3:4,5:6}
dict2 = {7:8,9:10}

dict1.update(dict2)

dict1["a"] = dict1.pop(1)

print(dict1)