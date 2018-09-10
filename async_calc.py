from threading import Thread
import calc
import model

def async_task():
  t = Thread(target=run)
  t.start()

def run():
  print("Calc", 'started')
  parties = model.get_party_records()
  individuals = model.get_individual_records()
  res = calc.calc_independent_candidates(individuals)
  model.update_history(dict(
    parties = parties,
    individuals = res
  ))
  print("Calc", 'finished')
