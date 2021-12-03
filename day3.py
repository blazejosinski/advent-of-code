from helpers import solve_line_task 

import numpy as np

def parse(line):
    a = np.zeros(len(line))
    for i in range(len(line)):
        if line[i] == '1':
            a[i] = 1
    return a

def compute_consumption(numbers):
    n = len(numbers)
    digits = len(numbers[0])
    sums = np.sum(numbers, axis=0)
    s1 = ""
    s2 = ""
    for i in range(digits):
        if sums[i] > n // 2:
            s1 += "1"
            s2 += "0"
        else:
            s1 += "0"
            s2 += "1"
    return int(s1, 2) * int(s2, 2)

def compute_co2(numbers):
    return select(numbers, True) * select(numbers, False)

def select(numbers, prefer_more):
    digits = len(numbers[0])
    for i in range(digits):
        if len(numbers) == 1:
            break
        sums = np.sum(numbers, axis=0)
        num_ones = sums[i]
        num_zeros = len(numbers) - num_ones
        if prefer_more:
            if num_ones >= num_zeros:
                selected = 1
            else:
                selected = 0
        else:
            if num_zeros <= num_ones:
                selected = 0
            else:
                selected = 1
        numbers = [num for num in numbers if num[i] == selected]
    return int("".join([str(int(d)) for d in numbers[0]]), 2)


def main():
    print(solve_line_task("in0", parse, compute_co2))
    print(solve_line_task("in1", parse, compute_co2))

if __name__ == "__main__":
    main()
