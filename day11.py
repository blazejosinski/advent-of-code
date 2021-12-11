from helpers import solve_line_task 


def parse(line):
    return [ord(c)-ord('0') for c in line]


M = 10


def isin(a, b):
    return 0 <= a and a < M and 0 <= b and b < M


def simulate_flashes(lines, steps=-1):
    M = 10
    num_flashes = 0
    for step in range(1000000000 if steps == -1 else steps):
        exploded = []
        for i in range(M):
            for j in range(M):
                lines[i][j] += 1
                if lines[i][j] >= 10:
                    exploded.append((i,j))
        bfs = exploded.copy()
        while bfs:
            cur = bfs.pop()
            for x in range(cur[0]-1, cur[0]+2):
                for y in range(cur[1]-1, cur[1]+2):
                    if isin(x,y) and (x!=cur[0] or y!=cur[1]):
                        lines[x][y] += 1
                        if lines[x][y] == 10:
                            exploded.append((x,y))
                            bfs.append((x,y))
        for (x,y) in exploded:
            lines[x][y] = 0
        num_flashes += len(exploded)
        if len(exploded) == M*M and steps == -1:
            return step+1
    return num_flashes


def main():
    print(solve_line_task("in0", parse, simulate_flashes))
    print(solve_line_task("in1", parse, simulate_flashes))


if __name__ == "__main__":
    main()
