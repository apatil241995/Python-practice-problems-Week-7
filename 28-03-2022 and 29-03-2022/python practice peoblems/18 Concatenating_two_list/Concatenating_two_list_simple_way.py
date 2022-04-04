#simple way
# 1 using append 
lis1 = [1,2,3,4,5]
lis2 = [6,7,8,9,10]

for i in lis2:
  lis1.append(i)

print(lis1)

# 2 using extend
lis3 = [1,4,2,5,6]
lis4 = [2,4,5,6,7]

print(lis3.extend(lis4))

# 3 using + sign
lis5 = [5,6,7,8,9]
lis6 = [5,6,7,8,3,2]

print(lis5+lis6)
