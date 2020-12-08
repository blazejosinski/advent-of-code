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
