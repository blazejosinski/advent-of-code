import numpy as np

def single_step(cups):
  n = len(cups)

  def next_v(a):
    return a-1 if a>1 else n
  
  selected = cups[1:4]
  next = next_v(cups[0])
  while next in selected:
    next = next_v(next)
  inx = cups.index(next)
  return cups[4:inx+1] + selected + cups[inx+1:] + cups[0:1]


def solve(cups, steps):
  cups = [int(a) for a in cups]
  print(cups)
  for _ in range(steps):
    cups = single_step(cups)
    print(cups)
  inx = cups.index(1)
  return "".join([str(d) for d in cups[inx+1:]+cups[:inx]])


def next_v(a, n):
  return a-1 if a>1 else n


def single_step_successor(successor):
  current = successor[0]

  selected = []
  for _ in range(3):
    current = successor[current]
    selected.append(current)
  
  destination = next_v(successor[0], 10**6)
  while destination in selected:
    destination = next_v(destination, 10**6)
  
  # update links
  successor[successor[0]] = successor[selected[-1]]
  successor[selected[-1]] = successor[destination]
  successor[destination] = selected[0]

  successor[0] = successor[successor[0]]


def solve_successor_representation(cups, steps):
  # Build successor representation.
  successor = np.zeros(10**6+1, dtype=np.int32)
  cups = [int(a) for a in cups]
  current = cups[0]
  for prev, next in zip(cups, cups[1:]):
    successor[prev] = next
  successor[cups[-1]] = max(cups)+1
  for i in range(max(cups)+1, 10**6):
    successor[i] = i+1
  successor[10**6] = current
  successor[0] = current
  for _ in range(steps):
    single_step_successor(successor)
  a = successor[1]
  b = successor[a]
  a = int(a)
  b = int(b)
  return a*b


def main():
    print(solve_successor_representation("463528179", 10**7))


if __name__ == "__main__":
    main()
