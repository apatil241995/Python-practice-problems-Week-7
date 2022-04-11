try:
  chickens = int(input("No. of chikens: "))
  cows = int(input("No. of cows: "))
  pigs = int(input("No. of pigs: "))
  
  total_no_of_legs = (chickens*2)+(cows*4)+(pigs*4)

  print(total_no_of_legs)
except:
  print("Please entr a integer value")