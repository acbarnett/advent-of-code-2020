filename = "a-demo.txt"
filename = "a-input.txt"

def get_seats(name):
  all_seats = []

  with open(name, "r") as f:
    all_seats = [line.rstrip() for line in f]

  return all_seats

def get_positions(seat):
  front = seat[:7]
  side = seat[7:]

  position_front_str = front.replace('F', '0').replace('B', '1')
  position_front = int(position_front_str, 2)

  position_side_str = side.replace('L', '0').replace('R', '1')
  position_side = int(position_side_str, 2)

  return position_front, position_side

def get_score(front, side):
  return front * 8 + side

all_seats = get_seats(filename)
high_score = 0
for seat in all_seats:
  positions = get_positions(seat)
  score = get_score(*positions)
  if score > high_score:
    high_score = score

print(high_score)
