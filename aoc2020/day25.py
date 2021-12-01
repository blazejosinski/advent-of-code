import re

from helpers import solve_line_task 

MOD = 20201227

def break_code(numbers):
    global MOD
    r = 1
    rr = 1
    for exp in range(1, MOD):
        r = (r * 7) % MOD
        rr = (rr * numbers[1]) % MOD
        if r == numbers[0]:
            return rr

def main():
    print(solve_line_task("in1", int, break_code))
    print(solve_line_task("in", int, break_code))


if __name__ == "__main__":
    main()