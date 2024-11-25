def PartOne():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Position = [0, 0]
  Checklist = {(0, 0): 1}
  for Move in Content:
    if Move == '^':
      Position[0] += 1
    elif Move == '>':
      Position[1] += 1
    elif Move == 'v':
      Position[0] -= 1
    else:
      Position[1] -= 1
    
    Checklist[(Position[0], Position[1])] = 1
  
  return len(Checklist)

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Positions = [[0, 0], [0, 0]]
  Checklist = {(0, 0): 1}
  Turn = 0
  for Move in Content:
    if Move == '^':
      Positions[Turn][0] += 1
    elif Move == '>':
      Positions[Turn][1] += 1
    elif Move == 'v':
      Positions[Turn][0] -= 1
    else:
      Positions[Turn][1] -= 1
    
    Checklist[(Positions[Turn][0], Positions[Turn][1])] = 1
    Turn ^= 1
  
  return len(Checklist)

print(PartOne())
print(PartTwo())