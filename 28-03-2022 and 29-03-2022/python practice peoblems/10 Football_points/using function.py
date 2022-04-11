def Points_calc(wins,draws,losses):
  if type(wins)==int and type(draws)==int and type(losses) == int:
    if wins>=0 and draws>=0 and losses>=0:
      points = (wins*3)+(draws*1)
      return points
    else:
      return "Please enter positive values"
  else:
    return "Please enter integer value"

if __name__=="__main__":
  print(Points_calc(3,2,1))