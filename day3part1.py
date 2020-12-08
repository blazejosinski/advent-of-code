f = open("in", "r")

map = [l.strip() for l in f.readlines()]

ans = 0
x, y = 0, 0

maxx = len(map)
maxy = len(map[0])

while x < maxx:
  if map[x][y] == "#":
    ans += 1
  x += 1
  y = (y+3) % maxy

print(ans)

