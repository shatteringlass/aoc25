import math

DAY = 6
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False

OPS = {'*': math.prod , '+': sum}

def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines

def get_operations(lines):
    operations = {}
    for row in range(len(lines)):
        for col, operand in enumerate(lines[row].split()):
            operand = operand.strip()
            if not operand:
                continue
            operation = operations.setdefault(col, [])
            operation.append(operand)
    return operations


def part_one(lines):
    result = 0

    ops = get_operations(lines)

    for op in ops.values():
        *nums, fun = op
        result += OPS[fun](map(int, nums))

    return result


def part_two(lines):
    result = 0

    lines = list(map(list, zip(*lines)))[::-1]
    numbers = []

    for line in lines:
        *lin, e = line
        num = ''.join(lin)
        if num.strip():
            numbers.append(num)
        if e in OPS:
            result += OPS[e](map(int, numbers))
            numbers = []

    return result


def main():
    lines = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(lines)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(lines)}")


if __name__ == "__main__":
    main()
