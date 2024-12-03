from itertools import combinations

def Product(List):
  Result = 1
  for i in List:
    Result *= i
  return Result

def PartOne():
  Content = open("Input.txt").read().splitlines()

  Packages = [int(i) for i in Content]
  Packages.sort(reverse=True)
  WeightPerCompartment = sum(Packages) // 3
  MaxPackageCount = (len(Packages)-1) // 3
  
  LeastNumberOfPassangerPackages = 99
  SmallestQuantumEntanglement = 99999999999
  for i in range(1, MaxPackageCount):
    for Combination in combinations(Packages, i):
      if sum(Combination) == WeightPerCompartment:
        LeastNumberOfPassangerPackages = min(LeastNumberOfPassangerPackages, len(Combination))
        SmallestQuantumEntanglement = min(SmallestQuantumEntanglement, Product(Combination))

  return SmallestQuantumEntanglement
  
def PartTwo():
  Content = open("Input.txt").read().splitlines()

  Packages = [int(i) for i in Content]
  Packages.sort(reverse=True)
  WeightPerCompartment = sum(Packages) // 4
  MaxPackageCount = (len(Packages)-1) // 4
  
  LeastNumberOfPassangerPackages = 99
  SmallestQuantumEntanglement = 99999999999
  for i in range(2, MaxPackageCount):
    for Combination in combinations(Packages, i):
      if sum(Combination) == WeightPerCompartment:
        LeastNumberOfPassangerPackages = min(LeastNumberOfPassangerPackages, len(Combination))
        SmallestQuantumEntanglement = min(SmallestQuantumEntanglement, Product(Combination))

  return SmallestQuantumEntanglement
  
print(PartOne())
print(PartTwo())