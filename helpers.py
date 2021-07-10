import numpy as np

def read_grouped_lines(filename):
  with open(filename, "r") as f:
    lines = [l.strip() for l in f.readlines()]
    lines.append("")

  groups = []
  current_group = []
  for l in lines:
    if len(l):
      current_group.append(l)
    else:
      groups.append(current_group)
      current_group = []
  return groups


def solve_grouped_task(filename, solve_group_fun, aggregate_fun):
  groups = read_grouped_lines(filename)
  solved_groups = [solve_group_fun(g) for g in groups]
  return aggregate_fun(solved_groups)


def solve_line_task(filename, solve_line_fun, aggregate_fun):
  with open(filename, "r") as f:
    lines = [l.strip() for l in f.readlines()]
  solved_lines = [solve_line_fun(l) for l in lines]
  return aggregate_fun(solved_lines)


def deduce(map):
  res_map = {}
  while map:
      for key, l in map.items():
          if len(l) == 1:
              val = l[0]
              res_map[key] = val
              map.pop(key)
              with suppress(ValueError):
                  for l in map.values():
                      l.remove(val)
              break
  return res_map


class GameOfLife():
    def __init__(self, neighbors, rules, alive):
        self.neighbors = neighbors
        self.rules = rules
        self.alive = alive

    def generate_neighbors(self, cell):
        cell = np.array(cell)
        for neighbor in self.neighbors:
            neighbor += cell
            yield tuple(neighbor)

    def count_alive_neighbours(self, cell):
        counter = 0
        for neighbor in self.generate_neighbors(cell):
            if neighbor in self.alive:
                counter += 1
        return counter
    
    def single_move(self):
        new_alive = set()
        for for_whom, how_many_alive in self.rules:
            if for_whom == 1:
                for cell in self.alive:
                    if self.count_alive_neighbours(cell) in how_many_alive:
                        new_alive.add(tuple(cell))
            else:
                for cell in self.alive:
                    for neighbor in self.generate_neighbors(cell):
                        if neighbor in self.alive:
                            continue
                        if self.count_alive_neighbours(neighbor) in how_many_alive:
                            new_alive.add(tuple(neighbor))
        self.alive = new_alive

    def simulate(self, steps = 2):
        for _ in range(steps):
            self.single_move()