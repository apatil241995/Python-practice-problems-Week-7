class Sequence:
  def __init__(self,start,stop):
    self.start = start
    self.stop = stop
  
  def answer(self):
      ans = ''
      for i in range(self.start,self.stop,1):
        if i%7==0 and i%5!=0:
            ans += f"{i},"
      return ans

if __name__ == "__main__":
  try:
    start = int(input('Give starting no: '))
    stop = int(input('give stoping no: '))
    obj = Sequence(start,stop)
    print(obj.answer())
  except:
    print("Please enter integer values")