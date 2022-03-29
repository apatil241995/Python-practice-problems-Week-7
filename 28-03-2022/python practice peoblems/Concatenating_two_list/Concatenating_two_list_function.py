#using append
def append_lis(lis1,lis2):
  for i in lis2:
    lis1.append(i)
  return lis1

#using extend 
def extend_lis(lis2,lis3):
  lis2.extend(lis3)
  return lis2

#using + sign
def plue_lis(lis4,lis5):
  return lis4+lis5