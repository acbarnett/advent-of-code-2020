name = "a-input.txt"

def get_groups(name):
  groups = []
  with open(name, "r") as f:
    unbroken = f.read()
    groups = [s.strip() for s in unbroken.split("\n\n")]

  return groups

def get_questions_per_group(group):
  one_line = group.replace("\n", "")
  characters = [c for c in one_line]
  return set(characters)

groups = get_groups(name)

sum = 0
for group in groups:
  uniques = get_questions_per_group(group)
  sum = sum + len(uniques)

print("Sum of unique questions per group")
print(sum)
