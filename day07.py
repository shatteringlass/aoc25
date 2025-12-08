from functools import cache

DAY = 7
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

    beams = set()

    for rdx, line in enumerate(lines):
        for cdx, char in enumerate(line):
            if char == "S":
                beams.add(cdx)
            elif char == "^" and cdx in beams:
                result += 1
                beams.update({cdx - 1, cdx + 1})
                beams.remove(cdx)

    return result


@cache
def count_unique(row, col, grid):
    if row == len(grid) or col == len(grid[0]):
        return 1

    if grid[row][col] == "^":
        return count_unique(row + 2, col - 1, grid) + count_unique(
            row + 2, col + 1, grid
        )

    return count_unique(row + 1, col, grid)


def part_two(lines):
    grid = tuple(tuple(line.strip()) for line in lines)
    result = count_unique(0, lines[0].index("S"), grid)
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
