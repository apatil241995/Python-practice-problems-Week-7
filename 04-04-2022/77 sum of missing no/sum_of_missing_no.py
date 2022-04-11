def missing_no_sum(lis):
  missing_nos = []
  sum = 0
  if len(lis) > 0:  
    for i in range(lis[-1]):
      if i+1 in lis:
        continue
      else:
        missing_nos.append(i+1)
    for j in missing_nos:
      sum += j
    return f"Sum of missing nos {sum}"
  else:
    return "Entered list is empty"

if __name__ == "__main__":
  lis1 = [1, 3, 5, 7, 10]
  print(missing_no_sum(lis1))