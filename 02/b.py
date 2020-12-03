from lib import count_valid

# filename = "input-a-demo.txt"
filename = "input-a.txt"


def check_valid(first, second, char, password):
  match_count = 0
  if password[first - 1] is char:
    match_count += 1
  if password[second - 1] is char:
    match_count += 1
  return match_count == 1


count_of_valid_rules = count_valid(filename, check_valid)
print(count_of_valid_rules)
