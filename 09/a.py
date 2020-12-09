# preamble_length = 5
# filename = "input-a-demo.txt"

preamble_length = 25
filename = "input-a.txt"

def get_nums(name):
  nums = []
  with open(name, "r") as f:
    nums = [int(line.strip()) for line in f]

  return nums

def is_sum_of_prev(num_to_check, possible_components):
  for i in range(0, len(possible_components)):
    for j in range(i + 1, len(possible_components)):
      if possible_components[i] + possible_components[j] == num_to_check:
        return True
  return False


numbers = get_nums(filename)

print("Solution to part a")
for i in range(preamble_length, len(numbers)):
  if not is_sum_of_prev(numbers[i], numbers[i - preamble_length:i]):
    print(numbers[i])
    part_a_solution = numbers[i]
    break

print("Solution to part b")
for i in range(0, len(numbers)):
  match_found = False
  sum = numbers[i]
  for j in range(i+1, len(numbers)):
    sum += numbers[j]
    if sum == part_a_solution:
      valid_range = numbers[i:j+1]
      print(min(valid_range) + max(valid_range))
      match_found = True
      break
  if match_found:
    break
