import hashlib

def PartOne():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Solution = 0
  while hashlib.md5((Content + str(Solution)).encode()).hexdigest()[:5] != "00000":
    Solution += 1
  
  return Solution

def PartTwo():
  File = open("Input.txt", "r")
  Content = File.read()
  File.close()

  Solution = 0
  while hashlib.md5((Content + str(Solution)).encode()).hexdigest()[:6] != "000000":
    Solution += 1
  
  return Solution

print(PartOne())
print(PartTwo())