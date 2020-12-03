from lib import count_trees, get_rows
# name = 'a-demo.txt'
name = 'a-input.txt'

# Rules for counting
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

c1 = count_trees(get_rows(name), 1, 1)
c2 = count_trees(get_rows(name), 3, 1)
c3 = count_trees(get_rows(name), 5, 1)
c4 = count_trees(get_rows(name), 7, 1)
c5 = count_trees(get_rows(name), 1, 2)

print(c1 * c2 * c3 * c4 * c5)
