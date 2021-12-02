import re
from helpers import solve_line_task 

def parse(line):
    tokens = line.split(' ')
    dist = int(tokens[1])
    if tokens[0] == 'forward':
        return (dist, 0)
    if tokens[0] == 'up':
        return (0, -dist)
    if tokens[0] == 'down':
        return (0, dist)

def simulate_boat(actions):
    position = (0, 0)
    for (forward, downword) in actions:
        position = (position[0]+forward, position[1]+downword)
    return position[0]*position[1]

def simulate_boat_aim(actions):
    position = (0, 0)
    aim = 0
    for (forward, aim_change) in actions:
        if aim_change:
            aim += aim_change
        else:
            position = (position[0]+forward, position[1]+forward*aim)
    return position[0]*position[1]


def main():
  print(solve_line_task("in0", parse, simulate_boat_aim))
  print(solve_line_task("in1", parse, simulate_boat_aim))

if __name__ == "__main__":
    main()
