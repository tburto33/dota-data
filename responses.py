import requests
import json
# import pandas as pd

def get_heroes_id():
   url =  'https://api.opendota.com/api/heroes'
   r = requests.get(url).json()
   with open('heroes.json', 'w', encoding='utf-8') as file:
      json.dump(r, file, indent=4)


def convert_hero_id(dataframe):
   with open('heroes.json', 'r') as file:
      heroes = json.loads(file)
      for hero in dataframe['hero_id']:
         if hero == heroes['id']:
            dataframe.replace(to_replace=[hero], value=heroes['localized_name'])

def get_my_heroes():
   r = requests.get('https://api.opendota.com/api/players/80034246/heroes').json()
   with open('myHeroes.json', 'w') as file:
      json.dump(r, file, indent=4)
   