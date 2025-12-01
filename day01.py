DAY = 1
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False


def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines


def part_one(lines):
    result = 0
    pos = 50

    for line in lines:
        sgn = +1 if line[0] == "R" else -1
        steps = int(line[1:])
        pos += sgn * steps
        pos %= 100
        if pos == 0:
            result += 1

    return result


def part_two(lines):
    result = 0
    pos = 50

    for line in lines:
        sgn = +1 if line[0] == "R" else -1
        steps = int(line[1:])
        ticks = sgn * steps
        new_pos = pos + ticks
        full_rot = abs(new_pos) // 100  # realized rotations (regardless of direction)
        underflow = int(pos > 0 and new_pos <= 0)  # unrealized rotation past zero
        result += full_rot + underflow
        print(f"Moved {ticks} from {pos}, landed at {new_pos}")
        print(f"Full rotations: {full_rot} - Underflow: {underflow}")
        pos = new_pos % 100

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
