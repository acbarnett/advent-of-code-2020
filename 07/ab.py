import re
# name = "a-input-demo.txt"
name = "a-input.txt"

def get_list_of_bags(name):
  strings = []
  with open(name, "r") as f:
    strings = [line.rstrip() for line in f]

  return strings

def remove_trailing_bag_or_bags(str):
  return re.sub(r' bags?', '', str)

def parse_bag(description):
  bag, contents = [d.strip(' .') for d in description.split('contain')]
  bag = remove_trailing_bag_or_bags(bag)

  contents = [remove_trailing_bag_or_bags(s.strip()) for s in contents.split(',')]

  return [bag, contents]

def make_bag_dict(list_of_bag_descriptions):
  bag_dict = {}

  for description in list_of_bags:
    bag, contents = parse_bag(description)

    bag_dict[bag] = {}

    for content in contents:
      if content == 'no other':
        continue
      num, color = content.split(' ', 1)
      bag_dict[bag][color] = int(num)

  return bag_dict

def check_bag(dict_of_bags, color_to_search, color_to_find):
  if color_to_find in dict_of_bags[color_to_search]:
    return True
  for next_color_to_search in dict_of_bags[color_to_search]:
    if check_bag(dict_of_bags, next_color_to_search, color_to_find):
      return True
  return False

def check_for_color(dict_of_bags, color_to_check):
  bags_containing_color = 0
  for bag_color in dict_of_bags:
    is_present = check_bag(dict_of_bags, bag_color, color_to_check)
    if is_present:
      bags_containing_color += 1

  return bags_containing_color

def count_bags(dict_of_bags, color):
  bag_count = 0
  bag_to_count = dict_of_bags[color]
  
  for contained_bag_color in bag_to_count:
    bag_count += bag_to_count[contained_bag_color]
    bag_count += bag_to_count[contained_bag_color] * count_bags(dict_of_bags, contained_bag_color)
  
  return bag_count



list_of_bags = get_list_of_bags(name)
bag_dict = make_bag_dict(list_of_bags)

print('How many bags contain shiny gold bags? (Part A)')
print(check_for_color(bag_dict, 'shiny gold'))

print('How many bags are in a shiny gold bag? (Part B)')
print(count_bags(bag_dict, 'shiny gold'))
