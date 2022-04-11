class Converter:
  def __init__(self, num, string):
    self.num = num
    self.string = string
  
  def ans(self):
    # converting integer to dtring after appling type check
    if type(self.num) == int:
      int_to_str = str(self.num)
    else:
      return "Please give a integer value as num"
    
    # converting string to integer arter appling type check and checking the base of string
    if type(self.string)==str and self.string.isnumeric():
      str_to_int = int(self.string)
    else:
      return "Please give a string value with 10 base"
    
    # returning the result after checking types of outputs
    if type(int_to_str) == str and type(str_to_int) == int:
      return f"Number to string {int_to_str}, String to Number {str_to_int}"
    else:
      return "Somthing went wrong"


if __name__=="__main__":
  obj = Converter(10,"10")
  print(obj.ans())