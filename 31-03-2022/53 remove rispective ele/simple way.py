list1 = [1,2,3,4,'anish','vijay','patil',5,6,7,8,9,10,'hii','bye','hello',11,12,13,14,15,'a','b','c','d']
a = input("Enter the list element to remove: ")

if a.isnumeric():
  list1.remove(int(a))
else:
  list1.remove(a)

print(list1)