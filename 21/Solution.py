Weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
Armors = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
Rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

def WouldWin(Attack, Defence, BossHP, BossDamage, BossArmor):
  HP = 100
  while BossHP > 0 and HP > 0:
    BossHP -= max(1, Attack-BossArmor)
    HP -= max(1, BossDamage-Defence)
  
  if BossHP < 1:
    return True
  
  return False

def PartOne():
  Content = open("Input.txt").read().splitlines()
  BossHP = int(Content[0].split(": ")[1])
  BossDamage = int(Content[1].split(": ")[1])
  BossArmor = int(Content[2].split(": ")[1])

  MinimumCost = 99999
  for Weapon in Weapons:
    for Armor in Armors:
      for i, Ring1 in enumerate(Rings):
        for Ring2 in Rings[i+1:]:
          Cost = Weapon[0] + Armor[0] + Ring1[0] + Ring2[0]
          Attack = Weapon[1] + Armor[1] + Ring1[1] + Ring2[1]
          Defence = Weapon[2] + Armor[2] + Ring1[2] + Ring2[2]

          if WouldWin(Attack, Defence, BossHP, BossDamage, BossArmor):
            MinimumCost = min(Cost, MinimumCost)

  return MinimumCost

def PartTwo():
  Content = open("Input.txt").read().splitlines()
  BossHP = int(Content[0].split(": ")[1])
  BossDamage = int(Content[1].split(": ")[1])
  BossArmor = int(Content[2].split(": ")[1])

  MaximumCost = 0
  for Weapon in Weapons:
    for Armor in Armors:
      for i, Ring1 in enumerate(Rings):
        for Ring2 in Rings[i+1:]:
          Cost = Weapon[0] + Armor[0] + Ring1[0] + Ring2[0]
          Attack = Weapon[1] + Armor[1] + Ring1[1] + Ring2[1]
          Defence = Weapon[2] + Armor[2] + Ring1[2] + Ring2[2]

          if not WouldWin(Attack, Defence, BossHP, BossDamage, BossArmor):
            MaximumCost = max(Cost, MaximumCost)

  return MaximumCost

print(PartOne())
print(PartTwo())