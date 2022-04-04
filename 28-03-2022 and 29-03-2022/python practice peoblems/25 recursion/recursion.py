def recursion(string,n):
  print(string)
  i = n-1
  if i > 0:
    recursion(string,i)

recursion("anish",5)