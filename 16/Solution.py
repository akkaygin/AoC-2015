def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Aunts = dict()
  for Line in Content:
    Aunts[int(Line.split(' ')[1][:-1])] = {
      Line.split(' ')[2][:-1]: int(Line.split(' ')[3][:-1]),
      Line.split(' ')[4][:-1]: int(Line.split(' ')[5][:-1]),
      Line.split(' ')[6][:-1]: int(Line.split(' ')[7][:-1]),
    }

  Needle = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
  }

  for Number, Items in Aunts.items():
    Correct = True
    for Key, Value in Needle.items():
      if Key in Items and Value != Items[Key]:
        Correct = False
    if Correct:
      return Number

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Aunts = dict()
  for Line in Content:
    Aunts[int(Line.split(' ')[1][:-1])] = {
      Line.split(' ')[2][:-1]: int(Line.split(' ')[3][:-1]),
      Line.split(' ')[4][:-1]: int(Line.split(' ')[5][:-1]),
      Line.split(' ')[6][:-1]: int(Line.split(' ')[7][:-1]),
    }

  Needle = {
    "children": 3,
    #"cats": 7,
    "samoyeds": 2,
    #"pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    #"goldfish": 5,
    #"trees": 3,
    "cars": 2,
    "perfumes": 1,
  }

  for Number, Items in Aunts.items():
    Correct = True
    if "cats" in Items and Items["cats"] <= 7:
      Correct = False
    elif "trees" in Items and Items["trees"] <= 3:
      Correct = False
    elif "pomeranians" in Items and Items["pomeranians"] >= 3:
      Correct = False
    elif "goldfish" in Items and Items["goldfish"] >= 5:
      Correct = False
    else:
      for Key, Value in Needle.items():
        if Key in Items and Value != Items[Key]:
          Correct = False
    if Correct:
      return Number

print(PartOne())
print(PartTwo())