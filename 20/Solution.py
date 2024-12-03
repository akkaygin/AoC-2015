from math import sqrt

def PartOne():
  Content = open("Input.txt").read().strip()
  Target = int(Content) // 10

  House = 1
  while True:
    Presents = 0
    for Elf in range(1, int(sqrt(House))+1):
      if House % Elf == 0:
        Presents += Elf
        Presents += House / Elf
    
    if Presents > Target:
      return House

    House += 1

def PartTwo():
  Content = open("Input.txt").read().strip()
  Target = int(Content) // 11

  House = [1] * Target
  for i in range(2, Target):
    for j in range(min(Target//i, 50)):
      House[i*j] += i

    if House[i] >= Target:
      return i

print(PartOne())
print(PartTwo())