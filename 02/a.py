from lib import count_valid

filename = "input-a.txt"

def check_validity(low, high, character, password):
  c = password.count(character)
  return c >= low and c <= high

count_of_valid_rules = count_valid(filename, check_validity)
print(count_of_valid_rules)
