import copy
import re

from helpers import solve_line_task 

def parse_line(s):
    return s[0], int(s[1:])

DIRECTIONS = {
    "N": (1,0),
    "E": (0,1),
    "S": (-1,0),
    "W": (0,-1),
}

ORDER_R = "NESW"

def move_ship(instructions):
    loc = 0,0
    heading = 1
    for com, param in instructions:
        if com in "RL":
            shift = 1 if com == "R" else -1
            heading = (heading + shift*(param//90) + 4)%4
            continue
        if com == "F":
            dir = DIRECTIONS[ORDER_R[heading]]
        else:
            dir = DIRECTIONS[com]
        loc = (loc[0]+dir[0]*param, loc[1]+dir[1]*param,)
        #print(loc)
    return abs(loc[0])+abs(loc[1])

def rotate(waypoint, left):
    np = waypoint[1], -waypoint[0]
    if left == 90:
        return np
    return rotate(np, left-90)

def move_ship_waypoint(instructions):
    waypoint = 1,10
    loc = 0,0
    for com, param in instructions:
        if com in "RL":
            if com == "R":
                param = 360 - param
            waypoint = rotate(waypoint, param)
        elif com in ORDER_R:
            dir = DIRECTIONS[com]
            waypoint = (waypoint[0]+dir[0]*param, waypoint[1]+dir[1]*param)
        elif com == "F":
            loc = (loc[0]+waypoint[0]*param, loc[1]+waypoint[1]*param)
        else:
            print("ERROR")
        #print(loc, waypoint)
    return abs(loc[0])+abs(loc[1])


def main():
  print(solve_line_task("in1", parse_line, move_ship_waypoint))
  print(solve_line_task("in", parse_line, move_ship_waypoint))
  

if __name__ == "__main__":
    main()
