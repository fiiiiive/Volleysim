import random

class Player():
  def __init__(self, fname = None, lname = None, swing = None, block = None, defense = None, serve = None):
    self.fname = fname
    self.lname = lname
    self.team = None
    self.position = None
    self.stats = {"Swing": swing, "Block": block, "Defense": defense, "Serve": serve}
    self.stattotal = 0

  def __str__(self):
    return f'{self.fname} {self.lname}'

  def defineStats(self):
    if not self.position:
      self.position = random.choice(['OH', 'OPP', 'MB', 'S', 'L', 'DS'])
    if self.position == 'OH':
      self.stats["Swing"] = random.randint(9, 12)
      self.stats["Block"] = random.randint(6, 9)
      self.stats["Defense"] = random.randint(3, 6)
      self.stats["Serve"] = random.randint(1, 3)
    elif self.position == 'OPP':
      self.stats["Swing"] = random.randint(9, 12)
      self.stats["Block"] = random.randint(3, 6)
      self.stats["Defense"] = random.randint(1, 3)
      self.stats["Serve"] = random.randint(6, 9)
    elif self.position == 'MB':
      self.stats["Swing"] = random.randint(6, 9)
      self.stats["Block"] = random.randint(9, 12)
      self.stats["Defense"] = random.randint(1, 3)
      self.stats["Serve"] = random.randint(3, 6)
    elif self.position == 'S':
      self.stats["Swing"] = random.randint(1, 3)
      self.stats["Block"] = random.randint(3, 6)
      self.stats["Defense"] = random.randint(6, 9)
      self.stats["Serve"] = random.randint(9, 12)
    elif self.position == 'L':
      self.stats["Swing"] = random.randint(3, 6)
      self.stats["Block"] = random.randint(1, 3)
      self.stats["Defense"] = random.randint(9, 12)
      self.stats["Serve"] = random.randint(6, 9)
    elif self.position == 'DS':
      self.stats["Swing"] = random.randint(6, 9)
      self.stats["Block"] = random.randint(1, 3)
      self.stats["Defense"] = random.randint(9, 12)
      self.stats["Serve"] = random.randint(3, 6)
    self.stattotal = sum(list(self.stats.values()))
    return