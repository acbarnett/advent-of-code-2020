import re
from lib import get_all_passports, parse_passport

# filename = "input-a-demo.txt"
filename = "input-a.txt"

def validate_byr(str_year):
  year = int(str_year)
  return year >= 1920 and year <= 2002

def validate_iyr(str_year):
  year = int(str_year)
  return year >= 2010 and year <= 2020

def validate_eyr(str_year):
  year = int(str_year)
  return year >= 2020 and year <= 2030

def validate_height(h):
  unit = h[-2:]
  if unit != "cm" and unit != "in":
    return False

  measure = int(h[:-2])

  if unit == "cm":
    return measure >= 150 and measure <= 193

  if unit == "in":
    return measure >= 59 and measure <= 76

  return False


def validate_pid(pid):
  return re.match(r'^[0-9]{9}$', pid) is not None

def validate_hair_color(color):
  return re.match(r'^#[0-9a-f]{6}', color) is not None


def validate_eye_color(color):
  colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  return color in colors


required_fields_and_validators = [
  ["byr", validate_byr],
  ["iyr", validate_iyr],
  ["eyr", validate_eyr],
  ["hgt", validate_height],
  ["hcl", validate_hair_color],
  ["ecl", validate_eye_color],
  ["pid", validate_pid],
  # "cid"
]

def validate_passport(passport):
  for field_info in required_fields_and_validators:
    field, validator = field_info
    if field not in passport:
      return False
    if not validator(passport[field]):
      return False
    
  return True

validate_passport_count = 0

all_passports = get_all_passports(filename)
for p in all_passports:
  passport = parse_passport(p)
  if validate_passport(passport):
    validate_passport_count += 1


print(validate_passport_count)
