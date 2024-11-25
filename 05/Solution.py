import re

def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  NiceStrings = 0
  for Line in Content:
    if re.search(r"ab|cd|pq|xy", Line) is not None:
      continue
    
    if len(re.findall(r"a|e|i|o|u", Line)) < 3:
      continue

    if re.search(r"(.)\1", Line) is None:
      continue

    NiceStrings += 1
    
  return NiceStrings

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  NiceStrings = 0
  for Line in Content:
    if re.search(r"(..).*\1", Line) is None:
      continue

    if re.search(r"(.).\1", Line) is None:
      continue

    NiceStrings += 1
    
  return NiceStrings

print(PartOne())
print(PartTwo())