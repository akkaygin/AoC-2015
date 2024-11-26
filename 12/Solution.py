import re
import json

def PartOne():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Numbers = re.findall(r"(-?\d+)", Content)
  Numbers = [int(x) for x in Numbers]
  return sum(Numbers)

def RemoveRed(Input):
  if isinstance(Input, dict):
    return RemoveFromDict(Input)
  elif isinstance(Input, list):
    return RemoveFromList(Input)
  else:
    return Input

def RemoveFromDict(Dict):
  Result = {}
  if "red" not in Dict.values():
    for Key, Value in Dict.items():
      Result[Key] = RemoveRed(Value)
  return Result

def RemoveFromList(List):
  Result = []
  for Value in List:
    Result.append(RemoveRed(Value))
  return Result

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  InputJSON = json.loads(Content)
  RedRemoved = json.dumps(RemoveRed(InputJSON))

  Numbers = re.findall(r"(-?\d+)", RedRemoved)
  Numbers = [int(x) for x in Numbers]
  return sum(Numbers)

print(PartOne())
print(PartTwo())