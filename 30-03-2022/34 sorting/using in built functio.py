lis = [3,4,2,5,1,6,7,8,10]
lis_ = [3,4,2,5,1,6,7,8,10]

#ascending order
try:
  lis.sort()
except:
  print("All the elements in thr list must be of same datatype")

#descending order
try:
  lis_.sort(reverse=True)
except:
  print("All the elements in thr list must be of same datatype")

print("ascending",lis)
print("descending", lis_)
