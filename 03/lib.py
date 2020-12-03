tree = '#'


def get_rows(name):
  all_rows = []

  with open(name, "r") as f:
    all_rows = [line.rstrip() for line in f]

  for i in range(0, len(all_rows)):
    all_rows[i] = [c for c in all_rows[i]]

  return all_rows

def count_trees(rows, x_distance, y_distance):
  x = 0
  y = 0
  trees_hit = 0
  row_length = len(rows[0])

  while(y < len(rows)):
    if rows[y][x] == tree:
      trees_hit += 1
    x = (x + x_distance) % row_length
    y = y + y_distance

  print(trees_hit)