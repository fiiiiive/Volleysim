import random
from Player import Player
class Team():
    def __init__(self, name):
        self.name = name
        self.tier = 'C'
        self.teamStats = dict()
        self.bst = 0
        self.wins = 0
        self.losses = 0
        self.setwins = 0
        self.setlosses = 0
        self.winrate = 0
        self.position = 1
        self.dwins = 0 #defensive game wins
        self.owins = 0 #offensive game wins
        self.oss = [] #offensive season score
        self.dss = [] #defensive season score
        self.ospg = 0 # Offensive Score Per Game
        self.dspg = 0 # Defensive Score Per Game
        self.changes = [0, 0, 0, 0, 0]
        self.podiums = [0, 0, 0, 0, 0, 0]
        self.awards = [0, 0]
        self.lastfive = {}
        self.streak = 0
        self.starPlayer = None
        return

    def defStats(self, swing=None, block=None, defense=None, serve=None):
      if self.starPlayer is not None:
        self.teamStats["Swing"] = swing + self.starPlayer.stats["Swing"]
        self.teamStats["Block"] = block + self.starPlayer.stats["Block"]
        self.teamStats["Defense"] = defense + self.starPlayer.stats["Defense"]
        self.teamStats["Serve"] = serve + self.starPlayer.stats["Serve"]
        self.bst = sum(self.teamStats.values())
      else:
        self.teamStats["Swing"] = swing 
        self.teamStats["Block"] = block 
        self.teamStats["Defense"] = defense 
        self.teamStats["Serve"] = serve 
        self.bst = sum(self.teamStats.values())
      return    

    def printStats(self, seasonnum):
        print(f"{self.name}")
        print("************************")
        j = 0
        for i in self.teamStats.keys():
            print(f"{i} : {self.teamStats[i]}", end='      ')
            if seasonnum > 1:
              if self.changes[j] > 0:
                print(f'+{self.changes[j]} ', end='')
              elif self.changes[j] < 0:
                print(f' {self.changes[j]} ', end ='')
              
            print('\n')
            j += 1
        print(f'Stat Total : {self.bst}', end = '      ')
        if seasonnum > 1:
          if self.changes[4] > 0:
            print(f'+{self.changes[4]} ', end='')
          elif self.changes[4] < 0:
            print(f' {self.changes[4]} ', end ='')
        print('\n')
        print(f'Star Player: {self.starPlayer.fname} {self.starPlayer.lname} : {self.starPlayer.position}\n')
        print(f'Swing: {self.starPlayer.stats["Swing"]}', end = '      ')
        print(f'Block: {self.starPlayer.stats["Block"]}\n')
        print(f'Defense: {self.starPlayer.stats["Defense"]}', end = '      ')
        print(f'Serve: {self.starPlayer.stats["Serve"]}')
        print('\n')
        return

    def seasonChange(self, seasonnum):
        self.wins = 0
        self.losses = 0
        self.setwins = 0
        self.setlosses = 0
        self.position = 1
        self.dwins = 0
        self.owins = 0
        self.ospg = 0
        self.dspg = 0
        self.oss.clear()
        self.dss.clear()
        j = 0
        exp = 1
        if seasonnum > 1:
          if self.tier == 'C':
            exp = 1.5
          elif self.tier == 'B':
            exp = 1.25
        for i in self.teamStats:
            ch = random.randint(-1, 1)
            if ch == 1 or ch == -1:
                amt = random.randint(1, 5)
                amt = int(amt * ch * exp) if ch == 1 else int(amt * ch)
                self.teamStats[i] = self.teamStats[i] + amt
                self.changes[j] = amt
            else:
                self.changes[j] = 0
            j += 1  
        temp = self.bst
        self.bst = sum(self.teamStats.values())
        self.changes[4] = self.bst - temp
        self.streak = 0
        self.starPlayer.defineStats()
        return

    def updateStats(self):
      self.oss.append(self.owins)
      self.dss.append(self.dwins)
      self.ospg = sum(self.oss) // len(self.oss)
      self.dspg = sum(self.dss) // len(self.dss)
      self.owins = 0
      self.dwins = 0
      return

    def updateStreak(self, opp, score, wl):
      if wl is True:
        dub = 'W'
        if self.streak < 0:
          self.streak = 1
        else:
          self.streak += 1
      else:
        dub = 'L'
        if self.streak > 0:
          self.streak = -abs(1)
        else:
          self.streak -= 1
      self.lastfive[opp] = [dub, score]    
      if len(self.lastfive.keys()) > 5:
        temp = list(self.lastfive.keys())
        popper = temp[0]
        self.lastfive.pop(popper)
      return

    def trade(self, league, fnames, lnames):
      temp = random.randint(0, self.position + 5)
      if temp < 8:
        return
      else:
        tradeteam = random.choice(league.teams)
        while tradeteam.name == self.name:
          tradeteam = random.choice(league.teams)
        tradeplayer = self.starPlayer
        self.starPlayer = tradeteam.starPlayer
        tradeteam.starPlayer = tradeplayer
        print(f'League {league.tier} : {self.name} trade {tradeplayer.fname} {tradeplayer.lname} ({tradeplayer.position}) for {tradeteam.name}\'s {self.starPlayer.fname} {self.starPlayer.lname} ({self.starPlayer.position})\n')
        return