from helpers import solve_line_task 

import numpy as np

def parse(line):
    tokens = line.split()
    ans = []
    for i in range(0,3,2):
        ans.append([int(t) for t in tokens[i].split(",")])
    return ans

def compute_double_covered(coords):
    MAX = 1000
    map = np.zeros((MAX,MAX), dtype=np.int32)
    for coord in coords:
        print(coord)
        start = coord[0]
        stop = coord[1]
        if start[0] == stop[0]:
            incr = (0, 1)
            first = min(start[1], stop[1])
            last = max(start[1], stop[1])
            line = (start[0], 0)
        elif start[1] == stop[1]:
            incr = (1, 0)
            first = min(start[0], stop[0])
            last = max(start[0], stop[0])
            line = (0, start[1])
        else:
            continue
        for i in range(first, last+1):
            x = incr[0]*i + line[0]
            y = incr[1]*i + line[1]
            map[x,y] += 1
    res = 0
    for i in range(MAX):
        for j in range(MAX):
            if map[i,j] >= 2:
                res += 1
    return res


def compute_double_covered_with_diagonal(coords):
    MAX = 1000
    map = np.zeros((MAX,MAX), dtype=np.int32)
    for coord in coords:
        start = coord[0]
        stop = coord[1]
        if start[0] > stop[0] or (start[0] == stop[0] and start[1] > stop[1]):
            start, stop = stop, start
        dist = [stop[0]-start[0], stop[1]-start[1]]
        divisor = max(abs(dist[0]), abs(dist[1]))
        incr = (dist[0]//divisor, dist[1]//divisor)
        while True:
            map[start[0], start[1]] += 1
            if start == stop:
                break
            start[0] += incr[0]
            start[1] += incr[1]
  
    mask = np.full((MAX,MAX), 2, dtype=np.int32)
    return np.sum(map >= mask)

def main():
    print(solve_line_task("in1", parse, compute_double_covered_with_diagonal))


if __name__ == "__main__":
    main()
