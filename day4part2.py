import re

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

def valid_year(s, l, h):
  if not re.fullmatch("\d\d\d\d", s):
    return False
  y = int(s)
  return l <= y <= h 

def valid_height(s):
  if not re.fullmatch("\d+\w+", s):
    return False
  if s.endswith("cm"):
    h = int(s[:-2])
    return 150 <= h <= 193
  if s.endswith("in"):
    h = int(s[:-2])
    return 59<= h <= 76 
  return False

def valid_hcl(s):
  return re.fullmatch("#[0-9a-f]{6}", s)

def valid_pid(s):
  return re.fullmatch("\d{9}", s)

valid_rules = {
  "byr": lambda s: valid_year(s, 1920, 2002), 
  "iyr": lambda s: valid_year(s, 2010, 2020), 
  "eyr": lambda s: valid_year(s, 2020, 2030), 
  "hgt": valid_height,
  "hcl": valid_hcl,
  "ecl": lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
  "pid": valid_pid,
  "cid": lambda s: True,
}

f = open("in2", "r")

lines = [l.strip() for l in f.readlines()]

ans = 0

def valid_pas(pl):
  blob = " ".join(pl)
  tokens = blob.split(" ")
  if not expected.issubset(set([t.split(":")[0] for t in tokens])):
    return False
  passport_data = [t.split(":") for t in tokens]
  for key,value in passport_data:
    if not valid_rules[key](value):
      return False
  return True 

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
