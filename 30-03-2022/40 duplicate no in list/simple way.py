lis = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1,12,88,7,6,2]
#using dict to store the elements in list as key and their no of occurance as value
dict = {}
duplicate_ele = []

for i in lis:
  if dict.get(i):
    dict[i] += 1
  else:
    dict[i] = 1

#printing the keys with value grater than 1 which naturaly are duplicate elements
for k,v in dict.items():
  if v > 1:
    duplicate_ele.append(k)

print(duplicate_ele)