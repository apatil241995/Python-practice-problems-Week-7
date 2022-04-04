#simple way
integer =  int(input("Enter a Number: "))
string = str(input("Ennter a string: "))

int_to_str = str(integer)
str_to_int = int(string)

print(integer," in string ",int_to_str)
print(string, " in integer ", str_to_int)

#using function
def converter(num,strng):
  return f"Number to string {str(num)}, String to Number {int(strng)}"

#using class
class Converter:
  def __init__(self, num, string):
    self.num = num
    self.string = string
  
  def ans(self):
    s_to_n = int(self.string)
    n_to_s = str(self.num)
    return f"Number to string {n_to_s}, String to Number {s_to_n}"