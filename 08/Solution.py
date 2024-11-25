import re

def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Result = 0
  for Line in Content:
    Result += 2
    Result += 3 * len(re.findall(r"\\x[0-9a-f][0-9a-f]", Line))
    Result += len(re.findall(r"\\\\", Line))
    Result += len(re.findall(r"\\\"", Line[:-2]))
  
  return Result

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Result = 0
  for Line in Content:
    Result += 2
    Result += len(re.findall(r"\\", Line))
    Result += len(re.findall(r"\"", Line))
  
  return Result

print(PartOne())
print(PartTwo())