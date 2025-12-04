DAY = 4
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False

DIRECTIONS = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]


def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines


def find_rolls(lines):
    rolls = []
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "@":
                rolls.append((r, c))
    return rolls


def find_accessible(rolls):
    accessible = []
    for roll in rolls:
        cnt = 0
        for dxn in DIRECTIONS:
            if tuple(map(sum, tuple(zip(roll, dxn)))) in rolls:
                cnt += 1
            if cnt > 3:
                break
        if cnt < 4:
            accessible.append(roll)

    return accessible


def part_one(lines):
    result = len(find_accessible(find_rolls(lines)))
    return result


def part_two(lines):
    result = 0

    rolls = find_rolls(lines)
    removable = find_accessible(rolls)
    result += len(removable)
    while removable:
        rolls = set(rolls).difference(set(removable))
        removable = find_accessible(rolls)
        result += len(removable)

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
