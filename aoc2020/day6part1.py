f = open("in", "r")

lines = [l.strip() for l in f.readlines()]
lines.append("")

ans = 0

def count_group(declarations):
  selected = set()
  for dec in declarations:
    selected = selected.union(set(dec))
  return len(selected)

current_group = []
for l in lines:
  if len(l) == 0:
    ans += count_group(current_group)
    #print(count_group(current_group))
    current_group= []
  else:
    current_group.append(l)

print(ans)
