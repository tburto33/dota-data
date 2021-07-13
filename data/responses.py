import requests
import os

api_key = os.getenv('API_TOKEN')
my_id = os.getenv('ACCT_ID')

def get_recent_matches():
   r = requests.get(f' https://api.opendota.com/api/players/{my_id}/recentMatches?api_key={api_key}')
   print(r) 