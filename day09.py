DAY = 9
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = True


def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines


def part_one(lines):
    result = 0

    red_tiles = []

    for line in lines:
        y, x = line.split(",")
        y, x = int(y), int(x)
        for y0, x0 in red_tiles:
            area = (1 + abs(y - y0)) * (1 + abs(x - x0))
            result = max(result, area)
        red_tiles.append((y, x))

    return result


def part_two(lines):
    result = 0

    red_tiles = []
    rectangles = []

    for line in lines:
        y, x = line.split(",")
        y, x = int(y), int(x)
        red_tiles.append((y, x))

    for y0, x0 in red_tiles:
        for y1, x1 in red_tiles[::-1]:
            min_x, max_x = min(x0, x1), max(x0, x1)
            min_y, max_y = min(y0, y1), max(y0, y1)
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    if (y, x) not in red_tiles:
                        break
                    else:
                        continue

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
