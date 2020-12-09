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


program_state = {
  ACC_VALUE: 0,
  CUR_LINE: 0,
  LINES_EXECUTED: []
}

def execute_a(state, lines):
  line = lines[state[CUR_LINE]]
  op, instruction = line.split(" ")
  instruction = int(instruction)

  if state[CUR_LINE] in state[LINES_EXECUTED]:
    return state[ACC_VALUE]

  if op == NOP:
    state[LINES_EXECUTED].append(state[CUR_LINE])
    state[CUR_LINE] += 1
    return execute_a(state, lines)

  if op == ACC:
    state[LINES_EXECUTED].append(state[CUR_LINE])
    state[CUR_LINE] += 1
    state[ACC_VALUE] += instruction
    return execute_a(state, lines)

  if op == JMP:
    state[LINES_EXECUTED].append(state[CUR_LINE])
    state[CUR_LINE] += instruction
    return execute_a(state, lines)




program_lines = get_lines(filename)

result = execute_a(program_state, program_lines)

print("Solution to part a")
print(result)