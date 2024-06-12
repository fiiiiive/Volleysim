import random
import os
import datetime
import time
class League():
  def __init__(self, teams, tier):
    self.teams = teams
    self.tier = tier
    self.seasonnum = 0
    self.weeknum = 0
    self.toptwo = []
    self.bottomtwo = []
    self.year = int(datetime.datetime.now().year)

  def playGame(self, a, b, winlim, playoffs, printresults, setmax):
    scorea = 0
    scoreb = 0
    setnum = 1
    scorelim = 25
    setscorea = 0
    setscoreb = 0
    endgame = False
    pointa = False
    pointb = False
    vals = ['Swing', 'Block', 'Defense', 'Serve']
    while endgame == False:
        if setnum == setmax:
          scorelim = 15
        while pointa == False and pointb == False:
            temp = random.randint(0, 3)
            val = vals[temp]
            playa = random.randint(0, list(a.teamStats.values())[temp])
            playb = random.randint(0, list(b.teamStats.values())[temp])
            if playa > playb:
              if val == 'Swing' or val == 'Serve':
                a.owins += 1
              else:
                a.dwins += 1
              pointa = True
                   
            if playb > playa:
              if val == 'Swing' or val == 'Serve':
                b.owins += 1
              else:
                b.dwins += 1
              pointb = True

        if pointa == True and pointb == False:
            scorea += 1

        if pointb == True and pointa == False:
            scoreb += 1

        pointa = False 
        pointb = False
        if scorea >= scorelim or scoreb >= scorelim:
            if scorea > scoreb:
                if scoreb > scorea - 2:
                    endgame = False
                else:
                    setscorea += 1
                    a.setwins += 1
                    b.setlosses += 1
                    #print(f"Set {setnum}")
                    if playoffs == True:
                      print(f'Score: {a.name} : {scorea} - {scoreb} : {b.name}')

                    #print(f'Sets:  {a.name} : {setscorea} - {setscoreb} : {b.name}')


                    if setscorea == winlim:
                        
                        endgame = True
                        if printresults:
                          print(f'\n{a.name} : {setscorea} - {setscoreb} : {b.name}')

                        if playoffs == True:
                          input()
                        a.updateStreak(b, f'{setscorea} - {setscoreb}',True)
                        b.updateStreak(a, f'{setscoreb} - {setscorea}', False)
                        return a, b
                    else:
                        if playoffs == True:
                          input()
                        endgame = False 
                        setnum += 1
                        scorea = 0
                        scoreb = 0
            elif scoreb > scorea: 
                if scorea > scoreb - 2:
                    endgame = False
                else:
                    setscoreb += 1
                    a.setlosses += 1
                    b.setwins += 1
                    #print(f"Set {setnum}")
                    if playoffs == True:
                      print(f'Score: {a.name} : {scorea} - {scoreb} : {b.name}')
                    #print(f'Sets:  {a.name} : {setscorea} - {setscoreb} : {b.name}')


                    if setscoreb == winlim:
                        
                        endgame = True
                        if printresults:
                          print(f'\n{a.name} : {setscorea} - {setscoreb} : {b.name}')

                        if playoffs == True:
                          input()
                        a.updateStreak(b, f'{setscorea} - {setscoreb}', False)
                        b.updateStreak(a, f'{setscoreb} - {setscorea}', True)
                        return b, a
                    else:
                        if playoffs == True:
                          input()
                        endgame = False
                        setnum += 1
                        scoreb = 0
                        scorea = 0
            else:
                endgame = False

  def watchGame(self, a, b, winlim, setmax):
    scorea = 0
    scoreb = 0
    setnum = 1
    scorelim = 25
    setscorea = 0
    setscoreb = 0
    endgame = False
    pointa = False
    pointb = False
    vals = ['Swing', 'Block', 'Defense', 'Serve']
    while endgame == False:
        if setnum == setmax:
          scorelim = 15
        while pointa == False and pointb == False:
            temp = random.randint(0, 3)
            val = vals[temp]
            playa = random.randint(0, list(a.teamStats.values())[temp])
            playb = random.randint(0, list(b.teamStats.values())[temp])
            if playa > playb:
              if val == 'Swing' or val == 'Serve':
                a.owins += 1
              else:
                a.dwins += 1
              pointa = True

            if playb > playa:
              if val == 'Swing' or val == 'Serve':
                b.owins += 1
              else:
                b.dwins += 1
              pointb = True

        if pointa is True and pointb is False:
            scorea += 1

        if pointb is True and pointa is False:
            scoreb += 1

        pointa = False 
        pointb = False
        os.system('clear')
        print(f"Set {setnum}")
        print(f'Score: {a.name} : {scorea} - {scoreb} : {b.name}')
        print(f'Sets:  {a.name} : {setscorea} - {setscoreb} : {b.name}')
        time.sleep(.25)
        if scorea >= scorelim or scoreb >= scorelim:
            if scorea > scoreb:
                if scoreb > scorea - 2:
                    endgame = False
                else:
                    setscorea += 1
                    a.setwins += 1
                    b.setlosses += 1
                    os.system('clear')
                    print(f"Set {setnum}")
                    print(f'Score: {a.name} : {scorea} - {scoreb} : {b.name}')
                    print(f'Sets:  {a.name} : {setscorea} - {setscoreb} : {b.name}')


                    if setscorea == winlim:
                        input()
                        endgame = True
                        os.system('clear')
                        print(f'\n{a.name} : {setscorea} - {setscoreb} : {b.name}')
                        input()
                        return a, b
                    else:
                        input('Press Enter to continue to next set')
                        endgame = False 
                        setnum += 1
                        scorea = 0
                        scoreb = 0
            elif scoreb > scorea: 
                if scorea > scoreb - 2:
                    endgame = False
                else:
                    setscoreb += 1
                    a.setlosses += 1
                    b.setwins += 1
                    os.system('clear')
                    print(f"Set {setnum}")
                    
                    print(f'Score: {a.name} : {scorea} - {scoreb} : {b.name}')
                    print(f'Sets:  {a.name} : {setscorea} - {setscoreb} : {b.name}')


                    if setscoreb == winlim:

                        endgame = True
                        input()
                        os.system('clear')
                        print(f'\n{a.name} : {setscorea} - {setscoreb} : {b.name}')
                        input()
                        return b, a
                    else:
                        input('Press Enter to continue to next set')
                        endgame = False
                        setnum += 1
                        scoreb = 0
                        scorea = 0
            else:
                endgame = False
  def week(self, weeknum, hometeams, awayteams, printresults = True):
    #choice for quickplay. quickplay = self.playGame w/o input()
    matchnum = 1
    if printresults == True:
      print('****************************************************************\n')
      for i, j in zip(hometeams, awayteams):
        print(f'Week {weeknum} - Match {matchnum}')
        winner, loser = self.playGame(i, j, 2, False, printresults, 3)
        winner.updateStats()
        loser.updateStats()
        winner.wins += 1
        loser.losses += 1
        matchnum += 1
        print('\n****************************************************************\n')
    else:
      for i, j in zip(hometeams, awayteams):
        winner, loser = self.playGame(i, j, 2, False, printresults, 3)
        winner.updateStats()
        loser.updateStats()
        winner.wins += 1
        loser.losses += 1
        matchnum += 1

  def printleague(self, league, weeknum, playoffs):            # Print Teams in Ranking Order
    largest = 0
    # setlargest = 0
    wrlargest = 0
    pos = 0
    topteams = list()
    for i in league:
        if i.setwins > 0:
            i.winrate = (i.setwins / (i.setwins + i.setlosses)) * 100.00
            i.winrate = round(i.winrate, 2)
        else:
            winrate = 0
        if i.wins > largest:
            largest = i.wins
            topteams.clear()
            topteams.append(i)
        elif i.wins == largest:
            if i.winrate > wrlargest:
                topteams.clear()
                wrlargest = i.winrate
                topteams.append(i)
            elif i.winrate == wrlargest:
                topteams.append(i)
        pos = self.rank(i)
        i.position = pos                                      
    txt10 = '---------------------------------- RELEGATION ZONE ----------------------------------\n'
    txt11 = '---------------------------------- PROMOTION  ZONE ----------------------------------\n'
    for j in range(11):
      if j == 3:
        if self.tier == 'C':
          print(txt11.center(125))
      if j == 9:
        if self.tier == 'A' or self.tier == 'B':
          if playoffs == False:
            print(txt10.center(125))
      for i in league:
        if i.position == j:
          txt = f'{i.name}' 
          txt2 = f'W: {i.wins}'
          txt3 = f'L: {i.losses}'
          txt4 = f'SW: {i.setwins}'
          txt5 = f'SL: {i.setlosses}'
          txt6 = f'WR: {i.winrate}%'
          txt7 = f'OSPG: {i.ospg}'
          txt8 = f'DSPG: {i.dspg}'
          txt9 = f'STRK: {i.streak}'
          txt12 = f'P. {i.position}'
          print(txt.center(10), txt2.center(10), txt3.center(10), txt4.center(10), txt5.center(10), txt6.center(10), txt7.center(20), txt8.center(20), txt9.center(20), txt12.rjust(10))
          print()
          
    print("League Leader(s): ")
    for i in topteams:
        print(i.name)    
        if weeknum == 21:
          i.podiums[3] += 1

  def rank(self, team):
    rank = 1
    for i in self.teams:
        if team.wins < i.wins:
            rank += 1
    return rank

  def playoffs(self):
    post = []
    loser = None
    for i in self.teams:
      if i.position <= 8:
        post.append(i)
    if len(post) == 8:
      for i in self.teams:
        if i not in post:
          self.bottomtwo.append(i)
      temp = post.copy()
      post.clear()
      for i in range(8):
        for j in temp:
          if j.position == i + 1:
            post.append(j)
      return post
    else:
      while len(post) > 8:
        hslosses = 0
        loser = None
        for i in post:
          if i.setlosses > hslosses:
            hslosses = i.setlosses
            loser = i
        post.remove(loser)
    for i in self.teams:
      if i not in post:
        self.bottomtwo.append(i)
    temp = post.copy()
    post.clear()
    for i in range(8):
      for j in temp:
        if j.position == i + 1:
          post.append(j)
    return post

  def championship(self, post, a, b, c, d, e, f, g, h, league):
    winlim = 2
    os.system('clear')
  #quarters
    print('****************************************************************\n')
    input(f'Quarterfinals - Match 1: ({post[a].position}) {post[a].name} v. {post[b].name} ({post[b].position})\n')
    winner1, loser1 = self.playGame(post[a], post[b], winlim, True, True, 3)
    os.system('clear')
    print('\n****************************************************************\n')
    input(f'Quarterfinals - Match 2: ({post[c].position}) {post[c].name} v. {post[d].name} ({post[d].position})\n')
    winner2, loser2 = self.playGame(post[c], post[d], winlim, True, True, 3)
    os.system('clear')
    print('\n****************************************************************\n')
    input(f'Quarterfinals - Match 3: ({post[e].position}) {post[e].name} v. {post[f].name} ({post[f].position})\n')
    winner3, loser3 = self.playGame(post[e], post[f], winlim, True, True, 3)
    os.system('clear')
    print('\n****************************************************************\n')
    input(f'Quarterfinals - Match 4: ({post[g].position}) {post[g].name} v. {post[h].name} ({post[h].position})\n')
    winner4, loser4 = self.playGame(post[g], post[h], winlim, True, True, 3)
    os.system('clear')
    print('\n****************************************************************\n')
  #semis
    winlim = 3
    input(f'Semifinals - Match 1: ({winner1.position}) {winner1.name} v. {winner2.name} ({winner2.position})\n')
    winner5, loser5 = self.playGame(winner1, winner2, winlim, True, True, 5)
    os.system('clear')
    print('\n****************************************************************\n')
    input(f'Semifinals - Match 2: ({winner3.position}) {winner3.name} v. {winner4.name} ({winner4.position})\n')
    winner6, loser6 = self.playGame(winner3, winner4, winlim, True, True, 5)
    os.system('clear')
    print('\n****************************************************************\n')
  #3rd
    input(f'Third Place Match: ({loser5.position}) {loser5.name} v. {loser6.name} ({loser6.position})\n')
    third, fourth = self.playGame(loser5, loser6, winlim, True, True, 5)
    os.system('clear')
    print('\n****************************************************************\n')
  #champ
    input(f'Championship: ({winner5.position}) {winner5.name} v. {winner6.name} ({winner6.position})\n')
    champ, runnerup = self.playGame(winner5, winner6, winlim, True, True, 5)
    os.system('clear')
    print('\n****************************************************************\n')
    txt1 = '************************************'
    txt2 = f'CHAMPION: {champ.name}'
    txt3 = f'SECOND PLACE: {runnerup.name}'
    txt4 = f'THIRD PLACE: {third.name}'
    if league == True:
      champ.podiums[0] += 1
      runnerup.podiums[1] += 1
      third.podiums[2] += 1
    if league == False:
      champ.podiums[4] += 1
    self.toptwo = [champ, runnerup]
    print(txt1.center(50))
    print(txt2.center(50))
    print(txt1.center(50))
    print(txt3.center(50))
    print(txt4.center(50))
    return

  def postawards(self):
    omax = self.teams[0]
    dmax = self.teams[0]
    for i in self.teams:
      if sum(i.oss) > sum(omax.oss):
        omax = i
      elif sum(i.oss) == sum(omax.oss):
        if i.setwins > omax.setwins:
          omax = i
      if sum(i.dss) > sum(dmax.dss):
        dmax = i
      elif sum(i.dss) == sum(dmax.dss):
        if i.setwins > dmax.setwins:
          dmax = i
          
    print(f'Offensive Team of the Year: {omax.name}          O-Score: {sum(omax.oss)}'.center(50))
    print(f'Defensive Team of the Year: {dmax.name}          D-Score: {sum(dmax.dss)}'.center(50))  
    omax.awards[0] += 1
    dmax.awards[1] += 1
    return  
    
  def printtoptwo(self):
    k = 0
    print('Up for Promotion:')
    while len(self.toptwo) < 2:
      k += 1
      for j in range(10):
        if self.teams[j].position == k:
          print(f'{self.teams[j].position}. {self.teams[j].name}')
          self.toptwo.append(self.teams[j])
          if len(self.toptwo) == 2:
            break
    return

  def viewTeam(self):
    chosen = None 
    team = input('Which team would you like to view? ')
    team = team.capitalize()
    for i in self.teams:
      if i.name == team:
        chosen = i
    while chosen == None:
      team = input(f'Team {team} not found. Which team would you like to view? ')
      team = team.capitalize()
      for i in self.teams:
        if i.name == team:
          chosen = i
    print(f'Team: {chosen.name}', end = '          ')
    print(f'League: {chosen.tier}\n')
    print(f'Wins: {chosen.wins}', end = '          ')
    print(f'Losses: {chosen.losses}\n')
    print(f'Set Wins: {chosen.setwins}', end = '          ')
    print(f'Set Losses: {chosen.setlosses}\n')
    print(f'Win Rate: {chosen.winrate}%\n')
    print(f'Offensive Score: {sum(chosen.oss)}', end = '          ')
    print(f'Defensive Score: {sum(chosen.dss)}\n')
    print(f'OSPG: {chosen.ospg}', end = '          ')
    print(f'DSPG: {chosen.dspg}\n')
    print(f'Position: {chosen.position}\n')
    print(f'Star Player: {chosen.starPlayer.fname} {chosen.starPlayer.lname} : {chosen.starPlayer.position}\n')
    print(f'Star Player Stats: \nSwing: {chosen.starPlayer.stats["Swing"]}\n')
    print(f'Block: {chosen.starPlayer.stats["Block"]}\n')
    print(f'Defense: {chosen.starPlayer.stats["Defense"]}\n')
    print(f'Serve: {chosen.starPlayer.stats["Serve"]}\n')
    print('Team Stats:\n')
    print(f'Swing: {chosen.teamStats["Swing"]}', end = '          ')
    print(f'Block: {chosen.teamStats["Block"]}\n')
    print(f'Defense: {chosen.teamStats["Defense"]}', end = '          ')
    print(f'Serve: {chosen.teamStats["Serve"]}\n')
    print(f'BST: {chosen.bst}\n')
    print(f'Last 5 Matches:')
    for i in chosen.lastfive.keys():
      print(f'{i.name}: Result: {chosen.lastfive[i]}')
    if chosen.streak >= 0:
      dub = 'W'
    else:
      dub = 'L'
    print(f'Streak: {dub}{abs(chosen.streak)}')
    input('Press Enter to Return')
    return
    