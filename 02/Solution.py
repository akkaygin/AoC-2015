def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  TotalPaperArea = 0
  for Line in Content:
    Length, Width, Height = [int(x) for x in Line.split('x')]
    SurfaceAreas = [Length * Width, Length * Height, Width * Height]
    Slack = min(SurfaceAreas)
    TotalPaperArea += 2 * sum(SurfaceAreas) + Slack
  
  return TotalPaperArea

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  TotalRibbonLength = 0
  for Line in Content:
    Dimensions = [int(x) for x in Line.split('x')]
    Volume = Dimensions[0] * Dimensions[1] * Dimensions[2]
    Dimensions.remove(max(Dimensions))
    ShortestPerimeter = 2 * sum(Dimensions)

    TotalRibbonLength += Volume + ShortestPerimeter
  
  return TotalRibbonLength
      
print(PartOne())
print(PartTwo())