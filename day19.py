import functools
import re

from helpers import solve_grouped_task


REGEXPDEF = ""

DEFINITIONS = {}

@functools.lru_cache(maxsize = 200)
def reg_repr(rule):
  definition = DEFINITIONS[rule]
  matches = re.findall("\"(\w)\"", definition)
  if len(matches) == 1:
    return matches[0]
  res = []
  for rules in definition.split("|"):
    res.append("("+("".join([reg_repr(int(r)) for r in rules.split()]))+")")
  return "("+("|".join(res))+")"


def count_correct_messages(rules_or_messages):
  global REGEXPDEF
  global DEFINITIONS
  if not REGEXPDEF:
    rules = rules_or_messages
    DEFINITIONS = {int(lhs): rhs.strip() for lhs, rhs in [r.split(":") for r in rules]}
    DEFINITIONS[8] = "|".join([" ".join(["42"]*i) for i in range(1,33)])
    DEFINITIONS[11] = "|".join([(" ".join(["42"]*i)+" "+" ".join(["31"]*i)) for i in range(1,17)])
    REGEXPDEF = reg_repr(0)
    print(REGEXPDEF)
  else:
    messages = rules_or_messages
    compiled = re.compile(REGEXPDEF)
    res = 0
    for message in messages:
      if compiled.fullmatch(message):
        res += 1
    return res


def main():
#  print(solve_grouped_task("in1", count_correct_messages, lambda x:x[1]))
  print(solve_grouped_task("in", count_correct_messages, lambda x:x[1]))
  #print(">",REGEXPDEF)
  #print(solve_grouped_task("in", count_group, sum))

if __name__ == "__main__":
  main()
