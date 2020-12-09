# filename = "input-demo-a.txt"
filename = "input-a.txt"

def get_lines(name):
  lines = []
  with open(name, "r") as f:
    lines = [line.strip() for line in f]

  return lines

NOP = "nop"
ACC = "acc"
JMP = "jmp"

ACC_VALUE = "ACC_VALUE"
CUR_LINE = "CUR_LINE"
LINES_EXECUTED = "LINES_EXECUTED"

def get_init_state():
  program_state = {
    ACC_VALUE: 0,
    CUR_LINE: 0,
    LINES_EXECUTED: []
  }
  return program_state

def flip_next_nop_or_jump(input_lines, start):
  lines = input_lines[:]
  for i in range(start, len(lines)):
    if lines[i].startswith(NOP):
      lines[i] = lines[i].replace(NOP, JMP)
      return lines, i + 1
    if lines[i].startswith(JMP):
      lines[i] = lines[i].replace(JMP, NOP)
      return lines, i + 1

  return lines, len(lines) + 1

def execute(state, lines, fail_on_infinite_loop):
  # This means the program has finished
  if state[CUR_LINE] >= len(lines):
    return state[ACC_VALUE]

  line = lines[state[CUR_LINE]]
  op, instruction = line.split(" ")
  instruction = int(instruction)

  # This means the program has encountered an infinite loop
  if state[CUR_LINE] in state[LINES_EXECUTED]:
    if fail_on_infinite_loop:
      return False
    else:
      return state[ACC_VALUE]

  if op == NOP:
    state[LINES_EXECUTED].append(state[CUR_LINE])
    state[CUR_LINE] += 1

  if op == ACC:
    state[LINES_EXECUTED].append(state[CUR_LINE])
    state[CUR_LINE] += 1
    state[ACC_VALUE] += instruction

  if op == JMP:
    state[LINES_EXECUTED].append(state[CUR_LINE])
    state[CUR_LINE] += instruction

  return execute(state, lines, fail_on_infinite_loop)


program_lines = get_lines(filename)

print("Solution to part a")
result = execute(get_init_state(), program_lines, False)
print(result)

print("Solution to part b")
line_to_search = 0
program_length = len(program_lines)
program_terminates = False
while line_to_search < program_length and not program_terminates:
  program, updated_line = flip_next_nop_or_jump(program_lines, line_to_search)
  line_to_search = updated_line

  result = execute(get_init_state(), program, True)

  if result is not False:
    program_terminates = True
    print(result)
