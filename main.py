import os
import random

from League import League
from Team import Team
from Player import Player


def main():
  print('''Welcome to the Volleysim!\nIn the volleyball infrastructure of this simulator, there are three leagues, League A, League B, and League C.\nEach league has a different set of rules and regulations:\n\nLeague C is the lowest tier. They play a 40 game season with the top two teams in the league being promoted to League B at the end of the regular season.\n\nLeague B is the second lowest tier. They play a 40 game season with the bottom two teams being relegated to League C at the end of the regular season. The top 8 teams remaining go into the playoffs, which is a standard quarterfinals (Best of 3), semis, and finals. The two teams that make it to the finals will also be promoted to League A.\n\nLeague A is the highest tier. They play a 40 game season, with the bottom two teams being relegated to League B at the end of the regular season. The top 8 teams remaining go into the playoffs, similar to League B. The League A championship is the highest honor in all of the Volleysim world, and the teams that achieve it are truly the best.\n\nThe teams in each league have different stats, including wins, Offensive-Score (O-Score), Defensive-Score (D-Score), Offensive Score per Game (OSPG), and Defensive Score per Game (DSPG). Each team has 4 stats that break down into Offensive stats (Serve and Swing), and Defensive stats (Block and Defense). In each game, a random stat will be picked along with a random number between 0 and that stats max value. Whichever team picks the higher stat value will win the point, and that stat will get a +1 to its Offensive or Defensive Score depending on the stat. The game is then a standard 2-out-of-3 game to 25 points, with the third set (or 5th for late playoffs) to 15. ''')
  input()
  fnames = ['Franny', 'Chrysostomos', 'Thom', 'Beau', 'Shelly', 'Nikolasz', 'Terry', 'Nolan', 'Vasileios', 'Rafael', 'Marshall', 'Leopold']
  lnames = ['Darby', 'Monday', 'Chiaki', 'Tristin', 'Reyes', 'Lavern', 'Ernst', 'Frederick', 'Darrow', 'Faddei', 'Derby', 'Yuzuru', 'Morris']
  
  x = [
      'Stampede', 'Mavericks', 'Novas', 'Sparks', 'Rogues', 'Spiders',
      'Dragons', 'Lynx', 'Guardians', 'Vandals'
  ]
  y = [
      'Shadows', 'Griffens', 'Vortex', 'Vipers', 'Gators', 'Swarm', 'Phantoms',
      'Strikers', 'Hydras', 'Hunters'
  ]
  z = [
      'Knights', 'Comets', 'Bolts', 'Storm', 'Stars', 'Sharks', 'Horizon', 
      'Wraiths', 'Behemoths', 'Serpents'
  ]
  topleague = list()
  botleague = list()
  lowerleague = list()
  play = 'y'
  try:
    with open('aleague.txt', 'r') as f:
      temp = f.readlines()
      snum = temp.pop(0)
      for i in temp:
        team = i.split()
        a = Team(team[0])
        a.tier = team[1]
        a.defStats(int(team[2]), int(team[3]), int(team[4]),     int(team[5]))
        a.podiums = [int(team[6]), int(team[7]), int(team[8]), int(team[9]), int(team[10]), int(team[11])]
        a.awards = [int(team[12]), int(team[13])]
        a.starPlayer = Player(team[14], team[15])
        a.starPlayer.position = team[16]
        topleague.append(a)
      f.close()
    with open('bleague.txt', 'r') as f:
        temp = f.readlines()
        for i in temp:
          team = i.split()
          b = Team(team[0])
          b.tier = team[1]
          b.defStats(int(team[2]), int(team[3]), int(team[4]), int(team[5]))
          b.podiums = [int(team[6]), int(team[7]), int(team[8]), int(team[9]), int(team[10]), int(team[11])]
          b.awards = [int(team[12]), int(team[13])]
          b.starPlayer = Player(team[14], team[15])
          b.starPlayer.position = team[16]
          botleague.append(b)
        f.close()
    with open('cleague.txt', 'r') as f:
      temp = f.readlines()
      for i in temp:
        team = i.split()
        c = Team(team[0])
        c.tier = team[1]
        c.defStats(int(team[2]), int(team[3]), int(team[4]), int(team[5]))
        c.podiums = [int(team[6]), int(team[7]), int(team[8]), int(team[9]), int(team[10]), int(team[11])]
        c.awards = [int(team[12]), int(team[13])]
        c.starPlayer = Player(team[14], team[15])
        c.starPlayer.position = team[16]
        lowerleague.append(c)
      f.close()
    aleague = League(topleague, 'A')
    bleague = League(botleague, 'B')
    cleague = League(lowerleague, 'C')
    aleague.seasonnum = int(snum) - 1
    bleague.seasonnum = int(snum) - 1
    cleague.seasonnum = int(snum) - 1
  except FileNotFoundError:
    for i, j, k in zip(x, y, z, strict=False): 
      a = Team(i)
      temp = Player(random.choice(fnames), random.choice(lnames))
      temp.defineStats()
      a.starPlayer = temp
      topleague.append(a)
      b = Team(j)
      temp = Player(random.choice(fnames), random.choice(lnames))
      temp.defineStats()
      b.starPlayer = temp
      botleague.append(b)
      c = Team(k)
      temp = Player(random.choice(fnames), random.choice(lnames))
      temp.defineStats()
      c.starPlayer = temp
      lowerleague.append(c)
    
      a.defStats(80, 80, 80, 80)
      b.defStats(80, 80, 80, 80)
      c.defStats(80, 80, 80, 80)
    aleague = League(topleague, 'A')
    bleague = League(botleague, 'B')
    cleague = League(lowerleague, 'C')
    
    for i in aleague.teams:
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.tier = 'A'
    for i in bleague.teams:
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.tier = 'B'
    for i in cleague.teams:
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
      i.seasonChange(0)
  volleysim = [aleague, bleague, cleague]
  print("League Created!")

  while play == 'y' or play == 'Y' or play == "":
    os.system('clear')
    aleague.seasonnum += 1
    print('A League')
    for i in aleague.teams:
      i.trade(aleague, fnames, lnames)
    input()
    for i in aleague.teams:
      i.seasonChange(aleague.seasonnum)
      i.printStats(aleague.seasonnum)
    input()
    os.system('clear')
    
    home = aleague.teams.copy()
    away = aleague.teams.copy()
    away = rotate(away)

    bleague.seasonnum += 1
    print('B League')
    for i in bleague.teams:
      i.trade(bleague, fnames, lnames)
    input()
    for i in bleague.teams:
      i.seasonChange(bleague.seasonnum)
      i.printStats(bleague.seasonnum)
    input()
    os.system('clear')
    bhome = bleague.teams.copy()
    baway = bleague.teams.copy()
    baway = rotate(baway)
    cleague.seasonnum += 1
    print('C League')
    for i in cleague.teams:
      i.trade(cleague, fnames, lnames)
    input()
    for i in cleague.teams:
      i.seasonChange(cleague.seasonnum)
      i.printStats(cleague.seasonnum)
    input()
    os.system('clear')
    chome = cleague.teams.copy()
    caway = cleague.teams.copy()
    caway = rotate(caway)
    print(f'Season {int(aleague.year + aleague.seasonnum)} Begins!')
    input()
    os.system('clear')
    aleague.weeknum = 0
    bleague.weeknum = 0
    cleague.weeknum = 0
    for i in range(40):
      aleague.weeknum += 1
      bleague.weeknum += 1
      cleague.weeknum += 1
      print(f'Week {aleague.weeknum}')
      aleague.week(aleague.weeknum, home, away, False)  #5
      bleague.week(bleague.weeknum, bhome, baway, False)  #5
      cleague.week(cleague.weeknum, chome, caway, False)  #5
      #os.system('clear')
      away = rotate(away)
      while home[0] == away[0]:
        away = rotate(away)
      baway = rotate(baway)
      while bhome[0] == baway[0]:
        baway = rotate(baway)
      caway = rotate(caway)
      while chome[0] == caway[0]:
        caway = rotate(caway)
      choice = '1'
      print('\n****************************************************************\n')
      print('League A')
      aleague.printleague(aleague.teams, aleague.weeknum, False)
      print('\n****************************************************************\n')
      print('League B')
      bleague.printleague(bleague.teams, bleague.weeknum, False)
      print('\n****************************************************************\n')
      print('League C')
      cleague.printleague(cleague.teams, cleague.weeknum, False)
      if aleague.weeknum % 10 == 0:
        while choice == '1':
          os.system('clear')
          print('\n****************************************************************\n')
          print('League A')
          aleague.printleague(aleague.teams, aleague.weeknum, False)
          print('\n****************************************************************\n')
          print('League B')
          bleague.printleague(bleague.teams, bleague.weeknum, False)
          print('\n****************************************************************\n')
          print('League C')
          cleague.printleague(cleague.teams, cleague.weeknum, False)
          choice = input('Week \nWhat would you like to do?\n1. View Team\n2. Continue\n')
          while choice != '1' and choice != '2' and choice != '':
            choice = input('Invalid Input\nWhat would you like to do?\n1. View Team\n2. Continue\n')
          if choice == '1':
            os.system('clear')
            liga = input('What League is the team you would like to view in? (A, B, C)\n')
            liga = liga.capitalize()
            while liga != 'A' and liga != 'B' and liga != 'C':
              liga = input('Invalid Input\nWhat League is the team you would like to view in? (A, B, C)\n')
              liga = liga.capitalize()
            for i in volleysim:
              if i.tier == liga:
                i.viewTeam()
              
      os.system('clear')
    os.system('clear')

    print('Playoffs!')
    aleague.weeknum += 1
    postseason = aleague.playoffs()
    bpostseason = bleague.playoffs()
    cpostseason = cleague.playoffs()
    print('Final League C Standings: ')
    cleague.printleague(cleague.teams, cleague.weeknum, True)
    print('Promoted to League B: ')
    cleague.printtoptwo()
    input()
    os.system('clear')
    print('Postseason Awards: ')
    print('League B')
    bleague.postawards()
    print('League A')
    aleague.postawards()
    input()
    os.system('clear')
    print('League B Playoffs Clinched')
    bleague.printleague(bpostseason, bleague.weeknum, True)
    print('Quarter Finals Matches:')
    print(f'Match 1: {bpostseason[0].name} ({bpostseason[0].position}) v. {bpostseason[7].name} ({bpostseason[7].position})')
    print(f'Match 2: {bpostseason[2].name} ({bpostseason[2].position}) v. {bpostseason[5].name} ({bpostseason[5].position})')
    print(f'Match 3: {bpostseason[1].name} ({bpostseason[1].position}) v. {bpostseason[6].name} ({bpostseason[6].position})')
    print(f'Match 4: {bpostseason[3].name} ({bpostseason[3].position}) v. {bpostseason[4].name} ({bpostseason[4].position})')
    input('B League Playoffs')
    bleague.championship(bpostseason, 0, 7, 2, 5, 1, 6, 3, 4, False)
    input()
    print('League A Playoffs Clinched')
    aleague.printleague(postseason, aleague.weeknum, True)
    print('Quarter Finals Matches:')
    print(f'Match 1: {postseason[0].name} ({postseason[0].position}) v. {postseason[7].name} ({postseason[7].position})')
    print(f'Match 2: {postseason[2].name} ({postseason[2].position}) v. {postseason[5].name} ({postseason[5].position})')
    print(f'Match 3: {postseason[1].name} ({postseason[1].position}) v. {postseason[6].name} ({postseason[6].position})')
    print(f'Match 4: {postseason[3].name} ({postseason[3].position}) v. {postseason[4].name} ({postseason[4].position})')
    input('A League Championship')
    aleague.championship(postseason, 0, 7, 2, 5, 1, 6, 3, 4, True)
    # OTOY AND DTOY
    
    play = input("Would you like to play another season? (Y/N) ")
    
    aleague.year += 1
    bleague.year += 1
    print('Relegated From League A: ')
    for i in aleague.bottomtwo:
      print(i.name)
    print('Promoted From League B: ')
    for i in bleague.toptwo:
      print(i.name)
    print('Relegated From League B: ')
    for i in bleague.bottomtwo:
      print(i.name)
    print('Promoted From League C: ')
    for i in cleague.toptwo:
      print(i.name)
    leagueswap(aleague, bleague, cleague)
    input()
  with open('aleague.txt', 'w') as f:
    f.write(str(aleague.seasonnum) + '\n')
    print("League A")
    print(f'Seasons: {aleague.seasonnum}')
    for i in aleague.teams:
      print(f'{i.name} : \nLeague A Championships: {i.podiums[0]}')
      print(f'League A Runner-up: {i.podiums[1]}')
      print(f'League A Third Place: {i.podiums[2]}')
      print(f'League A Regular Season Champions: {i.podiums[3]}')
      print(f'League A Offensive Team of the Year: {i.awards[0]}')
      print(f'League A Defensive Team of the Year: {i.awards[1]}')
      print(f'League B Champions: {i.podiums[4]}')
      print(f'League C Champions: {i.podiums[5]}')
      print()
      f.write(f'{i.name} {i.tier} {i.teamStats["Swing"]} {i.teamStats["Block"]} {i.teamStats["Defense"]} {i.teamStats["Serve"]} {i.podiums[0]} {i.podiums[1]} {i.podiums[2]} {i.podiums[3]} {i.podiums[4]} {i.podiums[5]} {i.awards[0]} {i.awards[1]} {i.starPlayer.fname} {i.starPlayer.lname} {i.starPlayer.position}\n')
    f.close()
    
  with open('bleague.txt', 'w') as f:
    print("League B")
    for i in bleague.teams:
      print(f'{i.name} : \nLeague A Championships: {i.podiums[0]}')
      print(f'League A Runner-up: {i.podiums[1]}')
      print(f'League A Third Place: {i.podiums[2]}')
      print(f'League A Regular Season Champions: {i.podiums[3]}')
      print(f'League A Offensive Team of the Year: {i.awards[0]}')
      print(f'League A Defensive Team of the Year: {i.awards[1]}')
      print(f'League B Champions: {i.podiums[4]}')
      print(f'League C Champions: {i.podiums[5]}')
      print()
      f.write(f'{i.name} {i.tier} {i.teamStats["Swing"]} {i.teamStats["Block"]} {i.teamStats["Defense"]} {i.teamStats["Serve"]} {i.podiums[0]} {i.podiums[1]} {i.podiums[2]} {i.podiums[3]} {i.podiums[4]} {i.podiums[5]} {i.awards[0]} {i.awards[1]} {i.starPlayer.fname} {i.starPlayer.lname} {i.starPlayer.position}\n')
    f.close()
    
  with open('cleague.txt', 'w') as f:
    print("League C")
    for i in cleague.teams:
      
      print(f'{i.name} : \nLeague A Championships: {i.podiums[0]}')
      print(f'League A Runner-up: {i.podiums[1]}')
      print(f'League A Third Place: {i.podiums[2]}')
      print(f'League A Regular Season Champions: {i.podiums[3]}')
      print(f'League A Offensive Team of the Year: {i.awards[0]}')
      print(f'League A Defensive Team of the Year: {i.awards[1]}')
      print(f'League B Champions: {i.podiums[4]}')
      print(f'League C Champions: {i.podiums[5]}')
      print()
      
      f.write(f'{i.name} {i.tier} {i.teamStats["Swing"]} {i.teamStats["Block"]} {i.teamStats["Defense"]} {i.teamStats["Serve"]} {i.podiums[0]} {i.podiums[1]} {i.podiums[2]} {i.podiums[3]} {i.podiums[4]} {i.podiums[5]} {i.awards[0]} {i.awards[1]} {i.starPlayer.fname} {i.starPlayer.lname} {i.starPlayer.position}\n')
    f.close()


def rotate(league):
  league.append(league.pop(0))
  return league

def leagueswap(topleague, botleague, cleague):
  for i in topleague.bottomtwo:
    i.tier = 'B'
    botleague.teams.append(i)
    topleague.teams.remove(i)
  for i in botleague.toptwo:
    i.tier = 'A'
    topleague.teams.append(i)
    botleague.teams.remove(i)
  for i in botleague.bottomtwo:
    i.tier = 'C'
    cleague.teams.append(i)
    botleague.teams.remove(i)
  for i in cleague.toptwo:
    i.tier = 'B'
    botleague.teams.append(i)
    cleague.teams.remove(i)
  input()
  topleague.toptwo.clear()
  botleague.toptwo.clear()
  topleague.bottomtwo.clear()
  botleague.bottomtwo.clear()
  cleague.toptwo.clear()
  cleague.bottomtwo.clear()
  return


if __name__ == "__main__":
  main()
