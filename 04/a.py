from lib import get_all_passports, parse_passport

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

validate_passport_count = 0

all_passports = get_all_passports(filename)
for p in all_passports:
  passport = parse_passport(p)
  if validate_passport(passport):
    validate_passport_count += 1


print(validate_passport_count)
