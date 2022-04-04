#method 1
tup = (1,2,3,4,5,6)

print(tup[::-1])

#method 2
tup1 = (7,8,9,10)

a = list(tup1)
a.reverse()
reverse_tup = tuple(a)

print(reverse_tup)