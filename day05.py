DAY = 5
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False

DIRECTIONS = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]


def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines


def parse_database(database):
    fresh = []
    avail = []
    for row in database:
        content = row.strip()
        if not content:
            continue
        elif "-" in content:
            l, r = content.split("-")
            fresh.append((int(l), int(r)))
        else:
            avail.append(int(content))
    print(
        f"Database built: {len(fresh)} ranges of fresh elements, {len(avail)} available elements"
    )
    return sorted(fresh, key=lambda x: (x[0], x[1])), avail


def part_one(lines):
    result = 0
    fresh, avail = parse_database(lines)
    for a in avail:
        for rng in fresh:
            first, last = rng
            if a < first or a > last:
                continue
            result += 1
            break
    return result


def part_two(lines):
    result = 0
    sorted_fresh, _ = parse_database(lines)

    prev_right = 0
    for left, right in sorted_fresh:
        new_right = max(prev_right, right) # to skip over fully overlapped ranges
        if left <= prev_right: # overlap
            result += new_right - prev_right
        else:
            result += right - left + 1
        prev_right = new_right
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
