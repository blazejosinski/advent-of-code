import numpy as np

from helpers import solve_line_task, GameOfLife

def simulate(map, steps = 6):
    alive = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                alive.append(np.array([0, i, j]))
    alive = set([tuple(a) for a in alive])
    neighbors = [(x,y,z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) if x or y or z]
    rules = [
        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
        # Otherwise, the cube becomes inactive.
        (1, [2,3]),
        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
        # Otherwise, the cube remains inactive.
        (0, [3]),
    ]
    gof = GameOfLife(neighbors=neighbors, rules=rules, alive=alive)
    gof.simulate(steps)
    return len(gof.alive)

def simulate_4d(map, steps = 6):
    alive = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                alive.append(np.array([0, 0, i, j]))
    alive = set([tuple(a) for a in alive])
    neighbors = [(x,y,z,t) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for t in range(-1,2) if x or y or z or t]
    rules = [
        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
        # Otherwise, the cube becomes inactive.
        (1, [2,3]),
        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
        # Otherwise, the cube remains inactive.
        (0, [3]),
    ]
    gof = GameOfLife(neighbors=neighbors, rules=rules, alive=alive)
    gof.simulate(steps)
    return len(gof.alive)

def main():
    #print(solve_line_task("in1", str, simulate))
    print(solve_line_task("in1", lambda x: x, simulate_4d))
    print(solve_line_task("in", lambda x: x, simulate_4d))


if __name__ == "__main__":
    main()