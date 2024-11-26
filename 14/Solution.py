def PartOne():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Farthest = 0
  for Line in Content:
    Velocity = int(Line.split(' ')[3])
    Burst = int(Line.split(' ')[6])
    Rest = int(Line.split(' ')[13])

    Distance = Velocity * Burst * int(2503 / (Burst + Rest))
    Distance += Velocity * min(2503 % (Burst + Rest), Burst)

    Farthest = max(Farthest, Distance)
  
  return Farthest

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Reindeers = dict()
  Scores = dict()
  DistanceCovered = dict()
  for Line in Content:
    Velocity = int(Line.split(' ')[3])
    Burst = int(Line.split(' ')[6])
    Rest = int(Line.split(' ')[13])
    Reindeers[Line.split(' ')[0]] = [Velocity, Burst, Rest]
    Scores[Line.split(' ')[0]] = 0
    DistanceCovered[Line.split(' ')[0]] = 0
  
  for t in range(1, 2503):
    Farthest = 0
    for Name, VBR in Reindeers.items():
      Velocity, Burst, Rest = VBR
      Distance = Velocity * Burst * int(t / (Burst + Rest)) + Velocity * min(t % (Burst + Rest), Burst)
      DistanceCovered[Name] = Distance
      Farthest = max(Farthest, Distance)

    for Name, Distance in DistanceCovered.items():
      if Distance == Farthest:
        Scores[Name] += 1
  
  return max(Scores.values())

print(PartOne())
print(PartTwo())