def parse_row(r):
  rule, password = [s.strip() for s in r.split(':')]
  rule_count, character = rule.split(' ')
  first, second = [int(n) for n in rule_count.split('-')]

  return [first, second, character, password]
  

def count_valid(name, validator):
  with open(name, "r") as f:
    all_rows = [line.rstrip() for line in f]

  valid_count = 0
  for row in all_rows:
    rule_details = parse_row(row)
    if validator(*rule_details):
      valid_count += 1

  return valid_count
