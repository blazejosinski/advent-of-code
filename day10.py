import re

from helpers import solve_line_task 

def naive_joltage(nums):
    nums = [0] + sorted(nums) + [max(nums) + 3]
    counts = [0] * 4
    for next, prev in zip(nums[1:], nums):
        counts[next-prev] += 1
    return counts[1]*counts[3]
    
def dp_joltage(nums):
    jolts = sorted(nums)
    final = max(jolts)
    counts = [0] * (final+1)
    counts[0] = 1
    for jolt in jolts:
        for i in range(1,4):
            if jolt-i >=0:
                counts[jolt] += counts[jolt-i] 
    return counts[final]

def main_1():
  print(solve_line_task("in1", int, naive_joltage))
  print(solve_line_task("in", int, naive_joltage))

def main_2():
  print(solve_line_task("in2", int, dp_joltage))
  print(solve_line_task("in1", int, dp_joltage))
  print(solve_line_task("in", int, dp_joltage))

if __name__ == "__main__":
    main_2()
