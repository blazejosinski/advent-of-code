f = open("in1.txt", "r")

nums = [int(a) for a in f.readlines()]

n = len(nums)

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if nums[i]+nums[j]+nums[k] == 2020:
        ans = nums[i] * nums[j] * nums[k], nums[i], nums[j], nums[k]

print(ans)
