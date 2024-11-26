from itertools import permutations

def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  People = set()
  Happiness = dict()
  for Line in Content:
    Who = Line.split(' ')[0]
    With = Line.split(' ')[-1][:-2]

    Mult = 1
    if Line.split(' ')[2] == "lose":
      Mult = -1

    Happiness[(Who, With)] = int(Line.split(' ')[3]) * Mult
    People |= {Who}
  
  MaximumHappiness = 0
  for Permutation in permutations(People):
    Permutation = Permutation + (Permutation[0], )
    TotalHappiness = 0
    TotalHappiness += sum(Happiness[Position] for Position in zip(Permutation, Permutation[1:]))
    TotalHappiness += sum(Happiness[Position] for Position in zip(Permutation[1:], Permutation))
    if TotalHappiness > MaximumHappiness:
      MaximumHappiness = TotalHappiness
  
  return MaximumHappiness

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  People = {"you"}
  Happiness = dict()
  for Line in Content:
    Who = Line.split(' ')[0]
    With = Line.split(' ')[-1][:-2]

    Mult = 1
    if Line.split(' ')[2] == "lose":
      Mult = -1

    Happiness[(Who, With)] = int(Line.split(' ')[3]) * Mult
    Happiness[(Who, "you")] = 0
    Happiness[("you", Who)] = 0
    People |= {Who}
  
  MaximumHappiness = 0
  for Permutation in permutations(People):
    Permutation = Permutation + (Permutation[0], )
    TotalHappiness = 0
    TotalHappiness += sum(Happiness[Position] for Position in zip(Permutation, Permutation[1:]))
    TotalHappiness += sum(Happiness[Position] for Position in zip(Permutation[1:], Permutation))
    if TotalHappiness > MaximumHappiness:
      MaximumHappiness = TotalHappiness
  
  return MaximumHappiness

print(PartOne())
print(PartTwo())