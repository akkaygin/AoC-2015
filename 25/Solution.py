def PartOne():
  Content = open("Input.txt").read().strip()

  Start = 20151125
  Multiply = 252533
  Divide = 33554393

  Row = int(Content.split()[-3][:-1])
  Column = int(Content.split()[-1][:-1])
  
  Index = Column + ((Row+Column-1) * (Row+Column-2) // 2)
  Result = Start
  for i in range(Index-1):
    Result = (Result * Multiply) % Divide
  
  return Result
  
print(PartOne())
