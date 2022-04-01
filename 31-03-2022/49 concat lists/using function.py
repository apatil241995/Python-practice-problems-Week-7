def cocn_list(l1,l2):
  output = []
  for i in l1:
    for j in l2:
      output.append(f"{i} {j}")
  return output

if __name__ == "__main__":
  list1 = ["Hello ", "take "]
  list2 = ["Dear", "Sir"] 

  print(cocn_list(list1,list2))