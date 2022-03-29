#simple way
chickens = int(input("No. of chikens: "))
cows = int(input("No. of cows: "))
pigs = int(input("No. of pigs: "))

total_no_of_legs = (chickens*2)+(cows*4)+(pigs*4)

print(total_no_of_legs)

#using function
def no_of_legs(chickens,cows,pigs):
  total_legs = (chickens*2)+(cows*4)+(pigs*4)
  return total_legs

#using class
class No_of_legson_farm:
  def __init__(self, chickens,cows,pigs):
    self.chickens = chickens
    self.cows = cows
    self.pigs = pigs
  
  def total_ans(self):
    total_no_of_legson_farm = (self.chickens*2)+(self.cows*4)+(self.pigs*4)
    return total_no_of_legson_farm