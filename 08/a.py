# filename = "input-demo-a.txt"
filename = "input-a.txt"

def get_lines(name):
  lines = []
  with open(name, "r") as f:
    lines = [line.strip() for line in f]

  return lines


program_state = {
  "acc": 0,
  "cur_line": 0,
  "lines_executed": []
}

def execute_a(state, lines):
  line = lines[state["cur_line"]]
  op, instruction = line.split(" ")
  instruction = int(instruction)

  if state["cur_line"] in state["lines_executed"]:
    return state["acc"]

  if op == "nop":
    state["lines_executed"].append(state["cur_line"])
    state["cur_line"] += 1
    return execute_a(state, lines)

  if op == "acc":
    state["lines_executed"].append(state["cur_line"])
    state["cur_line"] += 1
    state["acc"] += instruction
    return execute_a(state, lines)

  if op == "jmp":
    state["lines_executed"].append(state["cur_line"])
    state["cur_line"] += instruction
    return execute_a(state, lines)




program_lines = get_lines(filename)

result = execute_a(program_state, program_lines)

print("Solution to part a")
print(result)