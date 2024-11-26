from itertools import combinations

def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Containers = list()
  for Line in Content:
    Containers.append(int(Line[:-1]))
  
  Possibilities = 0
  for Length in range(len(Containers)-1):
    for i in combinations(Containers, Length):
      if sum(i) == 150:
        Possibilities += 1
  
  return Possibilities

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Containers = list()
  for Line in Content:
    Containers.append(int(Line[:-1]))
  
  Possibilities = 0
  for Length in range(len(Containers)-1):
    if Possibilities != 0:
      break

    for i in combinations(sorted(Containers), Length):
      if sum(i) == 150:
        Possibilities += 1
  
  return Possibilities
  
print(PartOne())
print(PartTwo())