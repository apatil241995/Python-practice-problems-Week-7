class Str_operation:

  def getString(self):
    try:
      string = str(input("Enter the string: "))
      self.string = string
      return self.string
    except:
      return "Please enter string value"
  
  def printString(self):
    print(self.string)

if __name__ == "__main__":   
  obj = Str_operation()
  obj.getString()
  obj.printString()