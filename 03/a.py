name = 'a-demo.txt'
name = 'a-input.txt'


tree = '#'

all_rows = []

with open(name, "r") as f:
  all_rows = [line.rstrip() for line in f]


for i in range(0, len(all_rows)):
  all_rows[i] = [c for c in all_rows[i]]

print(all_rows)


trees_hit = 0
x = 0
row_length = len(all_rows[0])
for i in range(0, len(all_rows)):
  print([i, x, row_length])
  if all_rows[i][x] == tree:
    trees_hit += 1
  x = (x + 3) % row_length

print(trees_hit)
