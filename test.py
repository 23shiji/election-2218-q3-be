import requests

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
for d in data:
  res = requests.post('http://localhost:8080/submit', json = d)
  pprint(res.text)

res = requests.get('http://localhost:8080/result')
pprint(res.json())