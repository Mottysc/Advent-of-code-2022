
def run_operations(input_file: str):
    with open(input_file, "r", encoding="utf-8") as puzzle_input:
        instructions = puzzle_input.read()

    x = 1
    for line in instructions.splitlines():
        yield x
        if line != "noop":
            yield x
            x += int(line[5:])


def part_1(input_file: str, width: int):
    interesting_signal_strength = []
    for cycle, x in enumerate(run_operations(input_file), 1):
        if cycle % width == 20:
            interesting_signal_strength.append(cycle * x)
    return sum(interesting_signal_strength)


def part_2(input_file: str, width: int):
    rows = []
    row_string = ""
    for cycle, x in enumerate(run_operations(input_file)):
        whatever = abs(cycle % width - x) < 2
        row_string += ".█"[whatever]
        if (cycle + 1) % width == 0:
            rows.append(row_string)
            row_string = ""

    for row in rows:
        print(row)


if __name__ == "__main__":
    part_1_ans = part_1(input_file="d10_input.txt", width=40)
    print(part_1_ans)

    part_2(input_file="d10_input.txt", width=40)
