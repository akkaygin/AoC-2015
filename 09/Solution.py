from itertools import permutations

def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Locations = set()
  Ways = dict()
  for Line in Content:
    From = Line.split(' ')[0]
    To = Line.split(' ')[2]
    Distance = int(Line.split(' ')[4])

    Locations |= {To, From}
    Ways[(From, To)] = Distance
    Ways[(To, From)] = Distance
  
  Minimum = 999999
  for Permutation in permutations(Locations):
    Length = sum(Ways[Route] for Route in zip(Permutation, Permutation[1:]))
    if Length < Minimum:
      Minimum = Length
  
  return Minimum

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Locations = set()
  Ways = dict()
  for Line in Content:
    From = Line.split(' ')[0]
    To = Line.split(' ')[2]
    Distance = int(Line.split(' ')[4])

    Locations |= {To, From}
    Ways[(From, To)] = Distance
    Ways[(To, From)] = Distance
  
  Maximum = 0
  for Permutation in permutations(Locations):
    Length = sum(Ways[Route] for Route in zip(Permutation, Permutation[1:]))
    if Length > Maximum:
      Maximum = Length
  
  return Maximum

print(PartOne())
print(PartTwo())