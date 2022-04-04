set1 = {1,2,3,4,5}
set2 = {1,6,7,3,8,2,9}

identical_ele = set({})

for i in set1:
  if i in set2:
    identical_ele.add(i)

print("set of identical items fron two sets is ",identical_ele)
