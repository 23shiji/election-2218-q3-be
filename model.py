import sqlite3
import json
from threading import Thread
from queue import Queue
import time
dbf = 'db.sqlite'


def auto_retry(func):
  def _func(*args, **kwargs):
    for _ in range(100):
      try:
        res =  func(*args, **kwargs)
      except sqlite3.OperationalError as err:
        print("Retry", err)
        time.sleep(1)
      else:
        return res
  return _func
@auto_retry
def check_ip(ip_address_checksum):
  db = sqlite3.connect(dbf)
  cursor = db.execute('''
  select count(*) from records
    where ip_checksum = ?;
  ''', [ip_address_checksum])
  r = cursor.fetchone()[0] != 0
  db.close()
  return r
@auto_retry
def create_record(ip_address_checksum, record):
  db = sqlite3.connect(dbf)
  db.execute('''
  insert into records values (?, ?);
  ''', [ip_address_checksum, json.dumps(record)])
  db.commit()
  db.close()
@auto_retry
def get_individual_records():
  db = sqlite3.connect(dbf)
  cursor = db.execute('''
  select content from records;
  ''')
  res = [
    json.loads(content)['independent_candidates']
    for (content,) in cursor
  ]
  db.close()
  return res
@auto_retry
def get_party_records():
  db = sqlite3.connect(dbf)
  cursor = db.execute('''
  select json_extract(content, '$.party_name') as pn, count(*) from records group by pn;
  ''')
  res = dict(cursor)
  db.close()
  return res
@auto_retry
def update_history(new_record):
  db = sqlite3.connect(dbf)
  db.execute('''
  insert into history values(?, CURRENT_TIMESTAMP);
  ''', [json.dumps(new_record)])
  db.commit()
  db.close()
@auto_retry
def get_lastest_history():
  db = sqlite3.connect(dbf)
  cursor = db.execute('''
  select content from history
    order by created_at desc limit 1;
  ''')
  r = cursor.fetchone()
  if r:
    r = r[0]
    res = json.loads(r)
  else:
    res = dict(
      parties = {},
      individuals = []
    )
  db.close()
  return res