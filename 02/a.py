filename = "input-a-demo.txt"
filename = "input-a.txt"


def check_validity(low, high, character, password):
  c = password.count(character)
  return c >= low and c <= high

def parse_row(r):
  rule, password = [s.strip() for s in r.split(':')]
  rule_count, character = rule.split(' ')
  low, high = [int(n) for n in rule_count.split('-')]

  return check_validity(low, high, character, password)
  

with open(filename, "r") as f:
  all_rows = [line.rstrip() for line in f]

valid_count = 0
for row in all_rows:
  if parse_row(row):
    valid_count += 1

print(valid_count)
