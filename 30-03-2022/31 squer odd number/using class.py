class Squre_of_odd_no:
  def __init__(self,lis):
    self.lis = lis
  
  def ans(self):
    if len(self.lis) == 20:
      try:
        answer = [i**2 for i in self.lis if i%2!=0]
        return answer
      except:
        return "Please provide list with all integer values"
    else:
      return "List is short expected list with  min length 20"
      
if __name__ == "__main__":
  list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  obj = Squre_of_odd_no(list_)
  print(obj.ans())