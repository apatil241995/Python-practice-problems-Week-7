l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28] 

def new_list(lis1,lis2):
  odd = [lis1[i] for i in range(len(lis1)) if i%2!=0]
  even = [lis2[j] for j in range(len(lis2)) if j%2==0]
  return odd+even


print(new_list(l1,l2))