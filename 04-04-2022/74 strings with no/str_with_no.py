def str_with_no(arr1):
  if len(arr1) > 0:
    arr2 = []
    for i in arr1:
      for j in i:
        if j.isnumeric():
          arr2.append(i)
          break
    return arr2
  else:
    return "Entered array is empty"

if __name__=="__main__":
  arr = ["anish","vij11ay","patil","Aliba3g"]
  print(str_with_no(arr))