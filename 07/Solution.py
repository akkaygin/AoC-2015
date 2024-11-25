def FindWire(Wires, Identifier):
  if Identifier in Wires:
    return Wires[Identifier]
  else:
    if Identifier.isdigit():
      return int(Identifier)
    else:
      return None

def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Wires = {}
  while "a" not in Wires:
    for Line in Content:
      SplitLine = Line.split(' ')
      Output = SplitLine[-1][:-1]
      if len(SplitLine) == 3:
        InputA = FindWire(Wires, SplitLine[0])
        if InputA is None:
          continue
          
        Wires[Output] = InputA
      elif len(SplitLine) == 4:
        InputA = FindWire(Wires, SplitLine[1])
        if InputA is None:
          continue

        Wires[Output] = 0xFFFF ^ InputA
      else:
        InputA = FindWire(Wires, SplitLine[0])
        if InputA is None:
          continue

        InputB = FindWire(Wires, SplitLine[2])
        if InputB is None:
          continue

        if SplitLine[1] == "AND":
          Wires[Output] = InputA & InputB
        elif SplitLine[1] == "OR":
          Wires[Output] = InputA | InputB
        elif SplitLine[1] == "RSHIFT":
          Wires[Output] = InputA >> InputB
        else:
          Wires[Output] = InputA << InputB
  
  return Wires["a"]

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Wires = {"b": PartOne()}
  while "a" not in Wires:
    for Line in Content:
      SplitLine = Line.split(' ')
      Output = SplitLine[-1][:-1]
      if len(SplitLine) == 3:
        if SplitLine[-1][0] == 'b':
          continue

        InputA = FindWire(Wires, SplitLine[0])
        if InputA is None:
          continue

        Wires[Output] = InputA
      elif len(SplitLine) == 4:
        InputA = FindWire(Wires, SplitLine[1])
        if InputA is None:
          continue

        Wires[Output] = 0xFFFF ^ InputA
      else:
        InputA = FindWire(Wires, SplitLine[0])
        if InputA is None:
          continue

        InputB = FindWire(Wires, SplitLine[2])
        if InputB is None:
          continue

        if SplitLine[1] == "AND":
          Wires[Output] = InputA & InputB
        elif SplitLine[1] == "OR":
          Wires[Output] = InputA | InputB
        elif SplitLine[1] == "RSHIFT":
          Wires[Output] = InputA >> InputB
        else:
          Wires[Output] = InputA << InputB
  
  return Wires["a"]

print(PartOne())
print(PartTwo())