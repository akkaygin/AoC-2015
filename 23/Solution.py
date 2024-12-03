def PartOne():
  Content = open("Input.txt").read().splitlines()

  Registers = {"a": 0, "b": 0}
  InstructionPointer = 0
  while InstructionPointer < len(Content):
    Line = Content[InstructionPointer]
    Instruction = Line.split()[0]

    if Instruction == "hlf":
      Registers[Line.split()[1]] //= 2
      InstructionPointer += 1
    elif Instruction == "tpl":
      Registers[Line.split()[1]] *= 3
      InstructionPointer += 1
    elif Instruction == "inc":
      Registers[Line.split()[1]] += 1
      InstructionPointer += 1
    elif Instruction == "jmp":
      InstructionPointer += int(Line.split()[1])
    elif Instruction == "jie":
      if Registers[Line.split()[1][0]] % 2 == 0:
        InstructionPointer += int(Line.split()[2])
      else:
        InstructionPointer += 1
    elif Instruction == "jio":
      if Registers[Line.split()[1][0]] == 1:
        InstructionPointer += int(Line.split()[2])
      else:
        InstructionPointer += 1

  return Registers["b"]

def PartTwo():
  Content = open("Input.txt").read().splitlines()

  Registers = {"a": 1, "b": 0}
  InstructionPointer = 0
  while InstructionPointer < len(Content):
    Line = Content[InstructionPointer]
    Instruction = Line.split()[0]

    if Instruction == "hlf":
      Registers[Line.split()[1]] //= 2
      InstructionPointer += 1
    elif Instruction == "tpl":
      Registers[Line.split()[1]] *= 3
      InstructionPointer += 1
    elif Instruction == "inc":
      Registers[Line.split()[1]] += 1
      InstructionPointer += 1
    elif Instruction == "jmp":
      InstructionPointer += int(Line.split()[1])
    elif Instruction == "jie":
      if Registers[Line.split()[1][0]] % 2 == 0:
        InstructionPointer += int(Line.split()[2])
      else:
        InstructionPointer += 1
    elif Instruction == "jio":
      if Registers[Line.split()[1][0]] == 1:
        InstructionPointer += int(Line.split()[2])
      else:
        InstructionPointer += 1

  return Registers["b"]

print(PartOne())
print(PartTwo())