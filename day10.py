import itertools


DAY = 10
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False

def parse_line(line):
    target, *buttons, joltage = line.split()
    target = tuple(int(l=='#') for l in target[1:-1])
    buttons = [(eval(x),) if isinstance(eval(x), int) else eval(x) for x in buttons]
    buttons = tuple(tuple(int(i in btn) for i in range(len(target))) for btn in buttons)
    return target, buttons, joltage

def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines

def tuple_to_bitmask(t):
    bitmask = 0
    for bit in t:
        bitmask <<= 1
        bitmask |= bit
    return bitmask

def part_one(lines):
    result = 0
    for line in tuple(parse_line(line) for line in lines):
        target, buttons = line
        target_bm = tuple_to_bitmask(target)
        buttons = tuple(tuple_to_bitmask(t) for t in buttons)
        all_off = tuple_to_bitmask(tuple(0 for _ in range(len(target))))
        i = 1
        found = False
        while not found:
            for combo in itertools.combinations_with_replacement(buttons, r=i):
                lights = all_off
                for btn in combo:
                    lights ^= btn
                    if lights == target_bm:
                        found = True
                if found:
                    break
            else:
                i += 1
                all_off = tuple_to_bitmask(tuple(0 for _ in range(len(target))))
        result += i
    return result


def part_two(lines):
    result = 0

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
