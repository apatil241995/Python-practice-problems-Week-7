list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
ans = " "
if len(list1) == len(list2):
  for i in range(len(list1)):
    ans += (f'{list1[i]+list2[i]} ')

print(ans)
