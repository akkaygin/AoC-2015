def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Lights = [[0 for Row in range(1000)] for Column in range(1000)]
  for Line in Content:
    Keyword = Line.split(' ')[-4]
    x1, y1 = [int(x) for x in Line.split(' ')[-3].split(',')]
    x2, y2 = [int(x) for x in Line.split(' ')[-1].split(',')]

    if Keyword == "on":
      for y in range(y1, y2+1):
        for x in range(x1, x2+1):
          Lights[x][y] = 1
    elif Keyword == "off":
      for y in range(y1, y2+1):
        for x in range(x1, x2+1):
          Lights[x][y] = 0
    else:
      for y in range(y1, y2+1):
        for x in range(x1, x2+1):
          Lights[x][y] ^= 1
  
  LitLights = sum(sum(Column) for Column in Lights)
  return LitLights

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Lights = [[0 for Row in range(1000)] for Column in range(1000)]
  for Line in Content:
    Keyword = Line.split(' ')[-4]
    x1, y1 = [int(x) for x in Line.split(' ')[-3].split(',')]
    x2, y2 = [int(x) for x in Line.split(' ')[-1].split(',')]

    if Keyword == "on":
      for y in range(y1, y2+1):
        for x in range(x1, x2+1):
          Lights[x][y] += 1
    elif Keyword == "off":
      for y in range(y1, y2+1):
        for x in range(x1, x2+1):
          if Lights[x][y] != 0:
            Lights[x][y] -= 1
    else:
      for y in range(y1, y2+1):
        for x in range(x1, x2+1):
          Lights[x][y] += 2
  
  TotalBrightness = sum(sum(Column) for Column in Lights)
  return TotalBrightness


print(PartOne())
print(PartTwo())