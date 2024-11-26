def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Lights = [[0 for _ in range(100)] for _ in range(100)]
  for y in range(100):
    for x in range(100):
      Lights[y][x] = 1 if Content[y][x] == '#' else 0

  for _ in range(100):
    LightsBuffer = [[0 for _ in range(100)] for _ in range(100)]
    for y in range(100):
      for x in range(100):
        LitNeighbors = 0
        for dy in range(-1, 2):
          if y + dy < 0 or y + dy > 99:
            continue
          for dx in range(-1, 2):
            if x + dx < 0 or x + dx > 99 or (dy == 0 and dx == 0):
              continue
            LitNeighbors += Lights[y + dy][x + dx]

        if Lights[y][x] == 1 and LitNeighbors > 1 and LitNeighbors < 4:
          LightsBuffer[y][x] = 1
        elif Lights[y][x] == 0 and LitNeighbors == 3:
          LightsBuffer[y][x] = 1
          
    Lights = LightsBuffer
  
  return sum(sum(Row) for Row in Lights)

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Lights = [[0 for _ in range(100)] for _ in range(100)]
  for y in range(100):
    for x in range(100):
      Lights[y][x] = 1 if Content[y][x] == '#' else 0
  
  Lights[0][0] = 1
  Lights[0][99] = 1
  Lights[99][0] = 1
  Lights[99][99] = 1

  for _ in range(100):
    LightsBuffer = [[0 for _ in range(100)] for _ in range(100)]
    for y in range(100):
      for x in range(100):
        LitNeighbors = 0
        for dy in range(-1, 2):
          if y + dy < 0 or y + dy > 99:
            continue
          for dx in range(-1, 2):
            if x + dx < 0 or x + dx > 99 or (dy == 0 and dx == 0):
              continue
            LitNeighbors += Lights[y + dy][x + dx]

        if Lights[y][x] == 1 and LitNeighbors > 1 and LitNeighbors < 4:
          LightsBuffer[y][x] = 1
        elif Lights[y][x] == 0 and LitNeighbors == 3:
          LightsBuffer[y][x] = 1

    LightsBuffer[0][0] = 1
    LightsBuffer[0][99] = 1
    LightsBuffer[99][0] = 1
    LightsBuffer[99][99] = 1
    Lights = LightsBuffer
  
  return sum(sum(Row) for Row in Lights)
  
print(PartOne())
print(PartTwo())