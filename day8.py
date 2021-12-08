from helpers import solve_line_task 

import numpy as np
import itertools


def solve_line(line):
    tokens = line.split()
    pos = tokens.index("|")
    output_digits = tokens[pos+1:]
    res = 0
    for digit in output_digits:
        if len(digit) in [2, 3, 4, 7]:
            res += 1
    return res


MAP_TO_DIGIT = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


LETTERS = "abcdefg"


def deduce(line):
    tokens = line.split()
    pos = tokens.index("|")
    input_digits = tokens[:pos]
    output_digits = tokens[pos+1:]
    for perm in itertools.permutations(LETTERS):
        wire_map = {l1: l2 for l1, l2 in zip(LETTERS, perm)}
        ok = True
        for digit in input_digits:
            decoded_digit = "".join(sorted([wire_map[d] for d in digit]))
            if decoded_digit not in MAP_TO_DIGIT:
                ok = False
                break
        if ok:
            break
    output_num = 0
    for digit in output_digits:
        decoded_digit = "".join(sorted([wire_map[d] for d in digit]))
        output_num = output_num*10 + MAP_TO_DIGIT[decoded_digit]
    return output_num


def main():
    print(solve_line_task("in1", deduce, sum))


if __name__ == "__main__":
    main()
