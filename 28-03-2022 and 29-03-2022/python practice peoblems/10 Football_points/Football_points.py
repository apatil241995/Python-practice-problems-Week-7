#simple way
wins = int(input('No of wins: '))
draws = int(input('No of draws: '))
losses = int(input('No of losses: '))

total_points = (wins*3)+(draws*1)
print(total_points)

#using function
def Points_calc(wins,draws,losses):
  points = (wins*3)+(draws*1)
  return points

#using class
class calc_points:
  def __init__(self, wins, draws, losses):
    self.wins = wins
    self.draws = draws
    self.losses = losses
  
  def ans(self):
    points = (wins*3)+(draws*1)
    return points