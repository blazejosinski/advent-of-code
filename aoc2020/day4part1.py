expected = set([
"byr",# (Birth Year)
"iyr",# (Issue Year)
"eyr",# (Expiration Year)
"hgt",# (Height)
"hcl",# (Hair Color)
"ecl",# (Eye Color)
"pid",# (Passport ID)
#"cid",# (Country ID)
])

f = open("in2", "r")

lines = [l.strip() for l in f.readlines()]

ans = 0

def valid_pas(pl):
  blob = " ".join(pl)
  tokens = blob.split(" ")
  if expected.issubset(set([t.split(":")[0] for t in tokens])):
    return True
  else:
    return False

current_pas = []
for l in lines:
  if len(l) == 0:
    ans += valid_pas(current_pas)
    current_pas = []
  else:
    current_pas.append(l)

if current_pas:
  ans += valid_pas(current_pas)

print(ans)
