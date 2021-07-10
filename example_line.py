import re

from helpers import solve_line_task 

def lookup(lb, up, desc):
  for c in desc:
    print(lb, up)
    print("->", c)
    if c == "F" or c == "L":
      up = (lb + up)//2
    else:
      lb = (lb + up)//2 + 1
  return up
  #print(up, lb)

def seat_number(s):
  return 8*lookup(0, 127, s[:7])+lookup(0,7, s[7:10])

def get_empty_seat(seats):
  seats = sorted(seats)
  old = -10
  for s in seats:
    if old+2 == s:
      return old+1
    old = s

def main():
  print(solve_line_task("in5", seat_number, max))
  print(solve_line_task("in5", seat_number, get_empty_seat))

if __name__ == "__main__":
    main()
