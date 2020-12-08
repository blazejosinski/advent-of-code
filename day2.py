f = open("in", "r")

inputs = f.readlines()

ans = 0
for line in inputs:
  nums, letter, password = line.split(" ")
  nums = nums.split("-")
  lb, up = int(nums[0]), int(nums[1])
  letter = letter[0]
  l_count = 0
  for ic in [lb, up]:
    if ic-1<len(password) and password[ic-1] == letter:
      l_count += 1
  if l_count == 1:
    ans += 1
#  if lb <= l_count and l_count <= up:
#    ans += 1  

print(ans)

