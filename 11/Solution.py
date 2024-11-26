import re

def HasStraight(Password):
  for i in range(len(Password)-3):
    Char1 = ord(Password[i+0])
    Char2 = ord(Password[i+1])
    Char3 = ord(Password[i+2])
    
    if Char1 == Char2 - 1 and Char3 == Char2 + 1:
      return True
  return False

def IncrementPassword(Password):
  NewPassword = list(Password)
  
  for i in range(len(Password)-1, -1, -1):
    if Password[i] == 'z':
      NewPassword[i] = 'a'
    else:
      NewPassword[i] = chr(ord(Password[i]) + 1)
      return "".join(NewPassword)

def PartOne():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Password = Content[:-1]
  while True:
    if HasStraight(Password):
      if not re.findall(r"i|o|l", Password):
        if re.findall(r"(.)\1.*(.)\2", Password):
          return Password
    
    Password = IncrementPassword(Password)

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.readlines()
  File.close()

  Password = IncrementPassword(PartOne())
  while True:
    if HasStraight(Password):
      if not re.findall(r"i|o|l", Password):
        if re.findall(r"(.)\1.*(.)\2", Password):
          return Password
    
    Password = IncrementPassword(Password)

print(PartOne())
print(PartTwo())