l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28] 

if len(l1)>0 and len(l2)>0:
  odd = [l1[i] for i in range(len(l1)) if i%2!=0]
  even = [l2[j] for j in range(len(l2)) if j%2==0]
else:
  print("list are empty")

new_lis = odd + even
print(new_lis)