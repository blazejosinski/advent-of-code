import re

from helpers import solve_line_task
from collections import Counter

moves = {
  "e": [0, 1],
  "se": [-1, 1],
  "sw": [-1, 0],
  "w": [0, -1],
  "nw": [1, -1],
  "ne": [1, 0],
}

def tile_coordinate(steps):
  cur = [0,0]
  inx = 0
  while inx < len(steps):
    if steps[inx:inx+1] in moves:
      move = moves[steps[inx:inx+1]]
      inx += 1
    else:
      move = moves[steps[inx:inx+2]]
      inx += 2
    cur[0] += move[0]
    cur[1] += move[1]
  return cur[0], cur[1]

def aggregate(tiles):
  c = Counter(tiles)
  black = 0
  for tile, count in c.items():
    if (count % 2) == 1:
      black += 1
  return black

def one_step(blacks):
  new_blacks = set()
  for black in blacks:
    #Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    count = 0
    for move in moves.values():
      if (black[0]+move[0], black[1]+move[1]) in blacks:
        count+=1
    if not (count == 0 or count > 2):
      new_blacks.add(black)
  
  for black in blacks:
    for move in moves.values():
      #Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
      potentially_white = (black[0]+move[0], black[1]+move[1])
      if potentially_white in blacks:
        continue
      count = 0
      for im in moves.values():
        if (potentially_white[0]+im[0], potentially_white[1]+im[1]) in blacks:
          count+=1
      if count == 2:
        new_blacks.add(potentially_white)
  return new_blacks


def simulate(tiles):
  counter = Counter(tiles)
  blacks = set()
  for tile, count in counter.items():
    if (count % 2) == 1:
      blacks.add(tile)
  for _ in range(100):
    blacks = one_step(blacks)
  return len(blacks)




def main():
  print(solve_line_task("in", tile_coordinate, aggregate))
  print(solve_line_task("in", tile_coordinate, simulate))

if __name__ == "__main__":
    main()
