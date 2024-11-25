def PartOne():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Floor = 0
  for Character in Content:
    if Character == '(':
      Floor += 1
    elif Character == ')':
      Floor -= 1
  
  return Floor

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Counter = 1
  Floor = 0
  for Character in Content:
    if Character == '(':
      Floor += 1
    elif Character == ')':
      Floor -= 1
    
    if Floor == -1:
      return Counter
    
    Counter += 1
      
print(PartOne())
print(PartTwo())