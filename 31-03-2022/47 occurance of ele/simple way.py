sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict = {}
for i in sample_list:
  if dict.get(i):
    dict[i] += 1
  else:
    dict[i] = 1
  
print(dict)