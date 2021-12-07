from helpers import solve_line_task 

import numpy as np

def parse(line):
    tokens = line.split(",")
    return [int(t) for t in tokens]

def compute_alingment(input):
    input = input[0]
    values, counts = np.unique(input, return_counts=True)
    ans = 0
    for v,c in zip(values[1:], counts[1:]):
        ans += (v - values[0])*c
    current_ans = ans
    left_group = counts[0]
    right_group = sum(counts[1:])
    last_v = values[0]
    for v,c in zip(values[1:], counts[1:]):
        current_ans += (v - last_v)*(left_group - right_group)
        left_group += c
        right_group -= c
        last_v = v
        if current_ans < ans:
            ans = current_ans
    return ans

def compute_alingment_expensive(input):
    input = input[0]
    values, counts = np.unique(input, return_counts=True)
    MAX = values[-1]
    distance_cost = np.zeros(MAX+1, dtype=np.int64)
    for i in range(1, MAX+1):
        distance_cost[i] = distance_cost[i-1]+i
    ans = None
    for pos in range(values[0], MAX+1):
        current_ans = 0
        for v,c in zip(values, counts):
            current_ans += distance_cost[abs(pos-v)]*c
        # print(pos, current_ans)
        if ans is None or ans > current_ans:
            ans = current_ans
    return ans


def main():
    print(solve_line_task("in0", parse, compute_alingment_expensive))
    print(solve_line_task("in1", parse, compute_alingment_expensive))


if __name__ == "__main__":
    main()
