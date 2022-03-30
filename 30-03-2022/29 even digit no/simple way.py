start = int(input("Enter the starting no: "))
stop = int(input("Enter the stoping no:"))
count = 0
list_ = []
for i in range(start,stop,1):
  a = str(i)
  for j in a:
    if int(j)%2==0:
      count += 1
  if count == len(a):
    count = 0
    list_.append(i)
  else:
    count = 0

ans = ','.join(list_)
print(ans)
