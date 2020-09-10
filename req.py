import requests


def get_intelligence(name):
    url = 'https://superheroapi.com/api/187702056088972/search/' + name
    response = requests.get(url)
    intellig = int(response.json()['results'][0]['powerstats']['intelligence'])
    intelligence_rating.update({name: intellig})


def print_most_intelligent():
  max_intelligence = max(intelligence_rating.values())
  for name, intelligence in intelligence_rating.items():
    if intelligence == max_intelligence:
      print(f'Самый умный {name} - {intelligence}')


intelligence_rating = {}
get_intelligence('hulk')
get_intelligence('thanos')
get_intelligence('captain america')
print_most_intelligent()