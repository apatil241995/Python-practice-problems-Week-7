program = input("enter the program: ")
lis = program.split(" ")
balance = 0
for i in range(len(lis)-1):
  if lis[i] == 'D':
    balance += int(lis[i+1])
  elif lis[i] == 'W':
    balance -= int(lis[i+1])

print(balance)