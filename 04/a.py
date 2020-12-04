filename = "input-a-demo.txt"
filename = "input-a.txt"


required_fields = [
  "byr",
  "iyr",
  "eyr",
  "hgt",
  "hcl",
  "ecl",
  "pid"
  # "cid"
]

def validate_passport(passport):
  for field in required_fields:
    if field not in passport:
      return False
  return True

def get_all_passports(name):
  passports = []

  with open(name, "r") as f:
    unbroken = f.read()
    passports = [s.strip() for s in unbroken.split("\n\n")]

  return passports

def parse_passport(passport_input):
  passport = {}
  for line in passport_input.split("\n"):
    entries = line.split(' ')
    for entry in entries:
      key, value = entry.split(':')
      passport[key] = value
  return passport

validate_passport_count = 0

all_passports = get_all_passports(filename)
for p in all_passports:
  passport = parse_passport(p)
  if validate_passport(passport):
    validate_passport_count += 1


print(validate_passport_count)
