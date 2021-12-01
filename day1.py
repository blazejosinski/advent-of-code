import re

from helpers import solve_line_task 

def count_increase(l):
  pairs = zip(l, l[1:])
  deeper = [x < y for x,y in pairs]
  return sum(deeper)

def count_increase_groups(l):
  sums = [a+b+c for a,b,c in zip(l, l[1:], l[2:])]
  return count_increase(sums)

def main():
  print(solve_line_task("in0", int, count_increase_groups))
  print(solve_line_task("in1", int, count_increase_groups))

if __name__ == "__main__":
    main()
