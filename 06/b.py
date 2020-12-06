name = "a-input.txt"

def get_groups(name):
  groups = []
  with open(name, "r") as f:
    unbroken = f.read()
    groups = [s.strip() for s in unbroken.split("\n\n")]

  return groups

def get_all_affirmatives_per_group(group):
  one_line = group.replace("\n", "")
  duplicate_questions = [c for c in one_line]
  questions = set(duplicate_questions)

  count = 0

  all_responses = group.split("\n")
  for question in questions:
    found_in_all = True
    for response in all_responses:
      if question not in response:
        found_in_all = False
    if found_in_all:
      count += 1

  return count

groups = get_groups(name)

sum = 0
for group in groups:
  all_yes = get_all_affirmatives_per_group(group)
  sum += all_yes

print("Sum of all affirmatively answered questions per group")
print(sum)
