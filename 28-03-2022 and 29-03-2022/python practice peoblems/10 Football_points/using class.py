class calc_points:
  def __init__(self, wins, draws, losses):
    self.wins = wins
    self.draws = draws
    self.losses = losses
  
  def ans(self):
    if type(self.wins)==int and type(self.draws)==int and type(self.losses) == int:
      if self.wins>=0 and self.draws>=0 and self.losses>=0:
        points = (self.wins*3)+(self.draws*1)
        return points
      else:
        return "Please enter positive values"
    else:
      return "Please enter integer value"

if __name__=="__main__":
  obj = calc_points(2,3,1)
  print(obj.ans())