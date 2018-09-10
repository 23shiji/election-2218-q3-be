import requests
import random
from threading import Thread

data = [
  {
    'party_name': 'YPP',
    'independent_candidates': [
      'VIFF',
      'laoweek'
    ]
  },
  {
    'party_name': 'JPY',
    'independent_candidates': [
      'wb',
      'laoweek'
    ]
  },
  {
    'party_name': 'YCP',
    'independent_candidates': [
      'wb',
      'wushi'
    ]
  },
  {
    'party_name': 'JPY',
    'independent_candidates': [
      'laoweek',
    ]
  },
]

from pprint import pprint

def run():
  d = random.choice(data)
  res = requests.post('http://localhost:8080/submit', json = d)
  pprint(res.text)

tl = [
  Thread(target=run)
  for _ in range(40)
]
for t in tl:
  t.start()
for t in tl:
  t.join()

res = requests.get('http://localhost:8080/result')
pprint(res.json())