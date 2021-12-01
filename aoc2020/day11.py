import copy
import re

from helpers import solve_line_task 

def one_step(map):
    n,m = len(map), len(map[0])
    res = copy.deepcopy(map)
    
    def isin(a,b):
        return 0 <= a < n and 0 <= b < m

    def occupied_n_count(map,a,b, debug=False):
        count = 0
        if debug:
            print(a,b, "-->")
        for ai in range(a-1, a+2):
            for bi in range(b-1, b+2):
                if isin(ai, bi) and map[ai][bi] == "#" and (ai != a or bi != b):
                    if debug: print(ai, bi)
                    count += 1
        return count

    for i in range(n):
        for j in range(m):
            if map[i][j] == 'L':
                if occupied_n_count(map,i,j) == 0:
                    res[i][j] = '#'
            elif map[i][j] == '#':
                if occupied_n_count(map,i,j) >= 4:
                    res[i][j] = 'L'
    return res

DIRECTIONS = [(x,y) for x in range(-1, 2) for y in range(-1,2) if x or y]
def get_adjacent_seats(map):
    n,m = len(map), len(map[0])
    
    def isin(a,b):
        return 0 <= a < n and 0 <= b < m

    adjacent_seats = []
    for i in range(n):
        acc = []
        for j in range(m):
            if map[i][j] == ".":
                acc.append([])
                continue
            cl = []
            for move in DIRECTIONS:
                pos = (i+move[0], j+move[1])
                while isin(*pos) and map[pos[0]][pos[1]] == '.':
                    pos = (pos[0]+move[0], pos[1]+move[1])
                if isin(*pos):
                    cl.append(pos)
            acc.append(cl)
        adjacent_seats.append(acc)
    return adjacent_seats

def one_step_part_2(map, adjacent_seats):
    n,m = len(map), len(map[0])
    res = copy.deepcopy(map)
    
    def isin(a,b):
        return 0 <= a < n and 0 <= b < m

    def occupied_n_count(a,b, debug=False):
        count = 0
        for (x,y) in adjacent_seats[a][b]:
            if map[x][y] == "#":
                count += 1
        return count

    for i in range(n):
        for j in range(m):
            if map[i][j] == 'L':
                if occupied_n_count(i,j) == 0:
                    res[i][j] = '#'
            elif map[i][j] == '#':
                if occupied_n_count(i,j) >= 5:
                    res[i][j] = 'L'
    return res

def simulate_chairs(map):
    map = [list(s) for s in map]
    adjacent_seats = get_adjacent_seats(map)
    z = 0 
    while True:
        z += 1
        # print("****")
        # print("\n".join(["".join(line) for line in map]))
        nmap = one_step_part_2(map, adjacent_seats)
        if nmap == map:
            break
        map = nmap
    return sum([s.count("#") for s in map]), z

def main():
  print(solve_line_task("in", lambda x: x, simulate_chairs))
  print(solve_line_task("in1", lambda x: x, simulate_chairs))

if __name__ == "__main__":
    main()
