from helpers import solve_line_task 

import numpy as np
import itertools


def parse(line):
    res = np.zeros(len(line), dtype=np.int32)
    for i in range(len(line)):
        res[i] = ord(line[i]) - ord('0')
    return res


MOVES = [(0,1), (1,0), (-1,0), (0, -1)]


def find_min(map):
    sum_min = 0
    n = len(map)
    m = len(map[0])
    for i in range(n):
        for j in range(m):
            ok = True
            for move in MOVES:
                move = (move[0]+i, move[1]+j)
                if 0 <= move[0] and move[0] < n and 0 <= move[1] and move[1] < m and map[move[0]][move[1]] <= map[i][j]:
                    ok = False
                    break
            if ok:
                sum_min += map[i][j] + 1
    return sum_min


def split_basins(map):
    basins_sizes = []
    n = len(map)
    m = len(map[0])
    visited = np.zeros((n,m), dtype=np.int32)
    for i in range(n):
        for j in range(m):
            if visited[i,j] or map[i][j] == 9:
                continue
            size = 1
            visited[i,j] = True
            queue = [(i,j)]
            while queue:
                v = queue[-1]
                queue.pop()
                for move in MOVES:
                    move = (move[0]+v[0], move[1]+v[1])
                    if 0 <= move[0] and move[0] < n and 0 <= move[1] and move[1] < m and not visited[move[0],move[1]] and map[move[0]][move[1]] < 9:
                        queue.append(move)
                        visited[move[0], move[1]] = True
                        size += 1
            basins_sizes.append(size)
    return np.prod(sorted(basins_sizes)[-3:])


def main():
    print(solve_line_task("in0", parse, split_basins))
    print(solve_line_task("in1", parse, split_basins))


if __name__ == "__main__":
    main()
