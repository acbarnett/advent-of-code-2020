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
    entries = line.split(" ")
    for entry in entries:
      key, value = entry.split(":")
      passport[key] = value
  return passport
