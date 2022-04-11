try:
  wins = int(input('No of wins: '))
  draws = int(input('No of draws: '))
  losses = int(input('No of losses: '))
  if wins >= 0 and draws >= 0 and losses >= 0:
    total_points = (wins*3)+(draws*1)
    print(total_points)
  else:
    print("Please enter a positive no")
except:
  print("please enter integer value")