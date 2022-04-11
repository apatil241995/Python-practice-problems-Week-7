#simple way
str1 = "anish"
str2 = "patil"

if len(str1) == len(str2):
  print(True)
else:
  print(False)

#using function
def comp_lenth(str3,str4):
  if len(str3) == len(str4):
    return True
  return False

#using class
class Comp_str:
  def __init__(self,str5,str6):
    self.str5 = str5
    self.str6 = str6
  
  def ans(self):
    if len(self.str5) == len(self.str6):
      return True
    return False
