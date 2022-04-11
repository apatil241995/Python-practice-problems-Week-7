sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

#using dict to store element as key and it's occurance as value
dict = {}


for i in sample_list:
  if dict.get(i):
    dict[i] += 1
  else:
    dict[i] = 1
  
print(dict)