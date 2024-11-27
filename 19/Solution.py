from collections import defaultdict

def PartOne():
  Content = open("Input.txt").read().splitlines()

  Replacements = defaultdict(list)
  for Line in Content[:-2]:
    Key, Value = Line.split(" => ")
    Replacements[Key].append(Value)
  
  Molecule = Content[-1]
  Results = set()
  for Base, ReplacementList in Replacements.items():
    Index = Molecule.find(Base)
    BaseLength = len(Base)
    while Index != -1:
      for Replacement in ReplacementList:
        Sub = Molecule[:Index] + Replacement + Molecule[Index+BaseLength:]
        Results.add(Sub)
      Index = Molecule.find(Base, Index+BaseLength)
  return len(Results)

def PartTwo():
  Content = open("Input.txt").read().splitlines()

  Molecule = Content[-1]
  # https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju/
  Elements = sum(C.isupper() for C in Molecule)
  Rn = Molecule.count("Rn")
  Y = Molecule.count("Y")
  return Elements - 2*Rn - 2*Y - 1

print(PartOne())
print(PartTwo())