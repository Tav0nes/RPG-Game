import json
from random import randint

list_npcs = []
inventory = []

player = {
  "Name": "Gustavo",
  "Level": 1,
  "XP": 0,
  "XP_max": 30,
  "HP": 100,
  "HP_max": 100,
  "Damage": 25,
  "Gold": 0,
  "Skills": {"Sword Mastery": 1},
  "Abilities": {"Seismic Smash": {"Damage": 50, "Cooldown": 3}}
}

def create_npcs(level):
  new_npc = {
    "Name": f"Monster #{level}",
    "Level": level,
    "Damage": 5 * level,
    "HP": 100 * level, 
    "HP_max": 100 * level, 
    "XP": 7 * level,
    "Gold": 10 * level,
  }
  return new_npc

def generate_npcs(n_npcs):
  for x in range(n_npcs):
    npc = create_npcs(x + 1)
    list_npcs.append(npc)


def print_all_npcs():
  for npc in list_npcs:
    print_npc()


def print_npc(npc):
  print(f"Name: {npc['Name']} // Level: {npc['Level']} // Damage: {npc['Damage']} // HP: {npc['HP']} // XP: {npc['XP']}")


def print_player():
  print(f"Name: {player['Name']} // Level: {player['Level']} // Damage: {player['Damage']} // HP: {player['HP']}/{player['HP_max']} // XP: {player['XP']}/{player['XP_max']} // Gold: {player['Gold']}g")


def reset_player():
  player['HP'] = player['HP_max']


def reset_npc(npc):
  npc['HP'] = npc['HP_max']


def level_up():
  if player['XP'] >= player['XP_max']:
    player['Level'] += 1
    player['XP'] = 0
    player['XP_max'] = player['XP_max'] * 2
    player['HP_max'] = player['HP_max'] * player['Level']
    player['Damage'] += 10
    print(f"{player['Name']} has leveled up to Level {player['Level']}!")



def start_battle(npc):
  while player['HP'] > 0 and npc['HP'] > 0:
    show_battle_info(npc)
    attack_npc(npc)
    if npc['HP'] <= 0:
      break
    attack_player(npc)
    print("-------------------------")
  
  if player['HP'] > 0:
    print("-------------------------")
    print(f"{player['Name']} has won and earned {npc['XP']} XP and {npc['Gold']}g!")
    player['XP'] += npc['XP'] 
    player['Gold'] += npc['Gold']
    print_player()
  else:
    print(f"The {npc['name']} has won.")
    print_npc(npc)

  level_up()
  reset_player()
  reset_npc(npc)


def attack_npc(npc):
  npc['HP'] -= player['Damage']
  print(f"{player['Name']} has attacked {npc['Name']} for {player['Damage']} damage")


def attack_player(npc):
  player['HP'] -= npc['Damage']
  print(f"{npc['Name']} has attacked {player['Name']} for {npc['Damage']} damage")


def show_battle_info(npc):
  print(f"{player['Name']} HP: {player['HP']}/{player['HP_max']}")
  print(f"{npc['Name']}: {npc['HP']}/{npc['HP_max']}")


def use_ability(npc, ability_name):
  if ability_name in player['Abilities']:
    ability = player['Abilities'][ability_name]
    if 'Cooldown' in ability and ability['Cooldown'] > 0:
      print(f"Ability {ability_name} is on cooldown.")
    else:
      npc['HP'] -= ability['Damage']
      print(f"{player['Name']} used {ability_name}, dealing {ability['Damage']} damage to {npc['Name']}!")
      ability['Cooldown'] = 3


def update_abilites():
  for ability in player['Abilities'].values():
    if 'Cooldown' in ability and ability['Cooldown'] > 0:
      ability['Cooldown'] -= 1


def save_player(filename='player_save.json'):
  with open(filename, 'w') as file:
    json.dump(player, file)
    print(f"Player progress saved to {filename}")


def load_player(filename='player_save.json'):
  global player
  try:
    with open(filename, 'w') as file:
      player = json.load(file)
      print(f"Player progress loaded from {filename}")
  except:
    print(f"No save file found with the name {filename}")


generate_npcs(5)
# show_npcs()

targeted_npc = list_npcs[0]
load_player()
start_battle(targeted_npc)
start_battle(targeted_npc)
start_battle(targeted_npc)
start_battle(targeted_npc)
start_battle(targeted_npc)
save_player()
print_player()
