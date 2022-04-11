class ConvertTo_intiger:
  def __init__(self, strng):
      self.strng = strng
    
  def ans(self):
    try:
      if type(self.strng) == str:
        ans = int(self.strng)
        return type(ans)
      else:
        return "Please enter a string"
    except:
      return "Please enter a string with base value 10"

if __name__=="__main__":
  obj = ConvertTo_intiger("10")
  print(obj.ans())