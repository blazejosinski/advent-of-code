f = open("in", "r")

map = [l.strip() for l in f.readlines()]

ans = 0

maxx = len(map)
maxy = len(map[0])

moves = [(1,1), (1,3), (1,5), (1,7), (2,1)]

final_ans = 1
for move in moves:
  ans = 0
  x, y = 0, 0
  while x < maxx:
    if map[x][y] == "#":
      ans += 1
    x += move[0] 
    y = (y+move[1]) % maxy
  final_ans *= ans

print(final_ans)
