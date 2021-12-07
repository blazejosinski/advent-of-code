from helpers import solve_line_task 

import numpy as np

def parse(line):
    tokens = line.split(",")
    return [int(t) for t in tokens]

def compute_number_of_fish(input, epoch=256):
    M = 10
    fish_ages = input[0]
    ages = np.zeros(M, dtype=np.int64)
    for i in fish_ages:
        ages[i] += 1
    for i in range(epoch):
        next_ages = np.zeros(M, dtype=np.int64)
        for j in range(1,M):
            next_ages[j-1] = ages[j]
        next_ages[8] = ages[0]
        next_ages[6] += ages[0]
        ages = next_ages
    return np.sum(ages)


def main():
    print(solve_line_task("in0", parse, compute_number_of_fish))
    print(solve_line_task("in1", parse, compute_number_of_fish))


if __name__ == "__main__":
    main()
