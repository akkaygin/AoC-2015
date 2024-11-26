def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Ingredients = dict()
  for Line in Content:
    Capacity   = int(Line.split(' ')[2][:-1])
    Durability = int(Line.split(' ')[4][:-1])
    Flavor     = int(Line.split(' ')[6][:-1])
    Texture    = int(Line.split(' ')[8][:-1])
    Ingredients[Line.split(' ')[0][:-1]] = [Capacity, Durability, Flavor, Texture]
  
  S = Ingredients["Sprinkles"]
  B = Ingredients["Butterscotch"]
  C1 = Ingredients["Chocolate"]
  C2 = Ingredients["Candy"]

  BestScore = 0
  for qS in range(100):
    for qB in range(100-qS):
      for qC1 in range(100-qS-qB):
        qC2 = 100-qS-qB-qC1
        CapacityScore   = max(0, S[0]*qS + B[0]*qB + C1[0]*qC1 + C2[0]*qC2)
        DurabilityScore = max(0, S[1]*qS + B[1]*qB + C1[1]*qC1 + C2[1]*qC2)
        FlavorScore     = max(0, S[2]*qS + B[2]*qB + C1[2]*qC1 + C2[2]*qC2)
        TextureScore    = max(0, S[3]*qS + B[3]*qB + C1[3]*qC1 + C2[3]*qC2)
        TotalScore      = CapacityScore * DurabilityScore * FlavorScore * TextureScore
        BestScore       = max(BestScore, TotalScore)
  
  return BestScore

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Ingredients = dict()
  for Line in Content:
    Capacity   = int(Line.split(' ')[2][:-1])
    Durability = int(Line.split(' ')[4][:-1])
    Flavor     = int(Line.split(' ')[6][:-1])
    Texture    = int(Line.split(' ')[8][:-1])
    Calories   = int(Line.split(' ')[10][:-1])
    Ingredients[Line.split(' ')[0][:-1]] = [Capacity, Durability, Flavor, Texture, Calories]
  
  S = Ingredients["Sprinkles"]
  B = Ingredients["Butterscotch"]
  C1 = Ingredients["Chocolate"]
  C2 = Ingredients["Candy"]

  BestScore = 0
  for qS in range(100):
    for qB in range(100-qS):
      for qC1 in range(100-qS-qB):
        qC2 = 100-qS-qB-qC1
        CapacityScore   = max(0, S[0]*qS + B[0]*qB + C1[0]*qC1 + C2[0]*qC2)
        DurabilityScore = max(0, S[1]*qS + B[1]*qB + C1[1]*qC1 + C2[1]*qC2)
        FlavorScore     = max(0, S[2]*qS + B[2]*qB + C1[2]*qC1 + C2[2]*qC2)
        TextureScore    = max(0, S[3]*qS + B[3]*qB + C1[3]*qC1 + C2[3]*qC2)
        TotalScore      = CapacityScore * DurabilityScore * FlavorScore * TextureScore
        Calories        = 1 if S[4]*qS + B[4]*qB + C1[4]*qC1 + C2[4]*qC2 == 500 else 0
        BestScore       = max(BestScore, TotalScore * Calories)
  
  return BestScore

print(PartOne())
print(PartTwo())