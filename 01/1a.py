with open("input-a.txt", "r") as f:
  all_entries = [int(line.strip()) for line in f]

for i in range(0, len(all_entries)):
  for j in range(i+1, len(all_entries)):
    if all_entries[i] + all_entries[j] == 2020:
      print(all_entries[i] * all_entries[j])
