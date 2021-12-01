import re

from helpers import solve_line_task 


def not_sum_of_last_25(numbers):
    for inx, value in enumerate(numbers):
        if inx < 25:  # preambule
            continue
        is_sum = False
        for i in range(1, 26):
            for j in range(i+1, 26):
                if numbers[inx-i]+numbers[inx-j] == value:
                    is_sum = True
        if not is_sum:
            return value

# Optimization with partial sums. Pessimistic runtime O(N^2).
def sum_to_large(numbers):
    SUM_TO = 3199139634
    partials = []
    part = 0
    for inx, value in enumerate(numbers):
        part += value
        partials.append(part)
        if part == SUM_TO and inx > 0:
            return min(numbers[:inx+1])+max(numbers[:inx+1])
    n = len(numbers)
    for start in range(n):
        for end in range(start+2, n):
            # # A brute-force alternative to partial sums:
            # if sum(numbers[start+1:end+1]) == SUM_TO:
            #     return min(numbers[start+1:end+1])+max(numbers[start+1:end+1])
            if partials[end]-partials[start] == SUM_TO:
               return min(numbers[start+1:end+1])+max(numbers[start+1:end+1])


def main():
  print(solve_line_task("in", int, not_sum_of_last_25))
  print(solve_line_task("in", int, sum_to_large))

if __name__ == "__main__":
    main()
