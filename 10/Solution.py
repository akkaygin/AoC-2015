import re

def PartOne():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Sequence = Content
  for _ in range(40):
    NewSequence = ""
    for Match in re.finditer(r"(\d)\1*", Sequence):
      NewSequence += str(len(Match[0])) + Match[0][0]
    Sequence = NewSequence
  
  return len(Sequence)

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Sequence = Content
  for _ in range(50):
    NewSequence = ""
    for Match in re.finditer(r"(\d)\1*", Sequence):
      NewSequence += str(len(Match[0])) + Match[0][0]
    Sequence = NewSequence
  
  return len(Sequence)

print(PartOne())
print(PartTwo())