class Str_operation:

  def getString(self):
    string = str(input("Enter the string: "))
    self.string = string
    return self.string
  
  def printString(self):
    print(self.string)

if __name__ == "__main__":   
  obj = Str_operation()
  obj.getString()
  obj.printString()