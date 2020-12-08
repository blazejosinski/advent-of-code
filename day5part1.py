import re

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
  pass

def main():
  f = open("in1", "r")
  
  lines = [l.strip() for l in f.readlines()]
  
  ans = 0
  for l in lines:
    ans = max(ans, seat_number(l))
  print(ans)

if __name__ == "__main__":
    main()
