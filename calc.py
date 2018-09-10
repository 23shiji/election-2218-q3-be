from functools import reduce
from collections import Counter
from operator import or_
def calc_independent_candidates(vote_results):
  order = []
  candidates = set(reduce(or_, map(set, vote_results)))
  while len(candidates) != 0:
    top = [
      r[-1]
      for r in vote_results
      if len(r) > 0 and r[-1] in candidates
    ]
    counter = Counter(top)
    last = min(counter.items(), key = lambda p: p[1])[0]
    order.append(last)
    candidates.remove(last)
    for r in vote_results:
      while r and (r[-1] == last or r[-1] not in candidates):
        r.pop()
  return list(reversed(order))
