import re
from helpers import solve_line_task 

class SolutionException(Exception):
    def __init__(self, value):
        self.value = value

def parse_line(s):
    tokens = s.split()
    return tokens[0], int(tokens[1])

def execute(lines):
    accumulator = 0
    nlines = len(lines)
    visited = [False] * nlines
    inx = 0
    while True:
        if inx == nlines:
            raise SolutionException(accumulator)
        if inx < 0 or inx > nlines:
            print("ERROR")
            return 0
        if visited[inx]:
            return accumulator
        visited[inx] = True
        command, param = lines[inx]
        if command == "jmp":
            inx += param
        else:
            inx += 1
            if command == "acc":
                accumulator += param

def fix_program(program):
    for inx, (command, param) in enumerate(program):
        if command == "acc":
            continue
        new_program = program.copy()
        new_program[inx] = ("jmp" if command == "nop" else "nop", param)
        try:
            execute(new_program)
        except SolutionException as solution:
            return solution.value

def main_1():
    print(solve_line_task("in1", parse_line, execute))
    print(solve_line_task("in", parse_line, execute))

def main_2():
    print(solve_line_task("in1", parse_line, fix_program))
    print(solve_line_task("in", parse_line, fix_program))


if __name__ == "__main__":
    main_1()
