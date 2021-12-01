import re

def binary_lookup(lb, up, desc):
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
  return 8*binary_lookup(0, 127, s[:7])+binary_lookup(0,7, s[7:10])

def main():
  f = open("in1", "r")
  
  lines = [l.strip() for l in f.readlines()]
  seats = sorted([seat_number(l) for l in lines]) 
  
  old = -10
  ans = 0
  for seat in seats:
    if old + 2 == seat:
      ans = old+1
    old = seat
  print(ans)

if __name__ == "__main__":
    main()
