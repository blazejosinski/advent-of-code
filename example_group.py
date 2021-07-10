from helpers import solve_grouped_task

def count_group(declarations):
  selected = set(declarations[0])
  for dec in declarations[1:]:
    selected = selected.intersection(set(dec))
  return len(selected)

def main():
  print(solve_grouped_task("in1", count_group, sum))
  print(solve_grouped_task("in", count_group, sum))

if __name__ == "__main__":
  main()
