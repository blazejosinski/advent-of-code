from helpers import solve_line_task 

import numpy as np
import itertools

PAIRS = {
    "(": ")",
    "{": "}",
    "<": ">",
    "[": "]",
}

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COMPLETION_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def points_per_line(line):
    st = []
    error = None
    for c in line:
        if c in PAIRS:
            st.append(c)
            continue
        if not st:
            error = c
            break
        if PAIRS[st[-1]] == c:
            st.pop()
        else:
            error = c
            break
    if error:
        return POINTS[error]
    return 0

def completion_per_line(line):
    st = []
    error = None
    for c in line:
        if c in PAIRS:
            st.append(c)
            continue
        if not st:
            error = c
            break
        if PAIRS[st[-1]] == c:
            st.pop()
        else:
            error = c
            break
    if error:
        return None
    res = 0
    while st:
        res = res*5 + COMPLETION_POINTS[PAIRS[st[-1]]]
        st.pop()
    return res


def select_middle(points):
    points = [p for p in points if p]
    points = sorted(points)
    return points[len(points)//2]

def main():
    print(solve_line_task("in0", completion_per_line, select_middle))
    print(solve_line_task("in1", completion_per_line, select_middle))


if __name__ == "__main__":
    main()
