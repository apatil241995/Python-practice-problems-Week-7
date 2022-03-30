def acc_balance(program):
  
  lis = program.split(" ")
  balance = 0
  for i in range(len(lis)-1):
    if lis[i] == 'D':
      balance += int(lis[i+1])
    elif lis[i] == 'W':
      balance -= int(lis[i+1])
  return balance

if __name__ == "__main__":
  program = input("enter the program: ")
  print(acc_balance(program)) 