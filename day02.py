DAY = 2
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

    for rng in lines[0].split(","):
        rng_start, rng_end = rng.split("-")
        for rid in range(int(rng_start), int(rng_end) + 1):
            rid_str = str(rid)
            if len(rid_str) % 2 == 0:
                if rid_str[: len(rid_str) // 2] == rid_str[len(rid_str) // 2 :]:
                    result += rid

    return result


def part_two(lines):
    result = 0

    for rng in lines[0].split(","):
        rng_start, rng_end = rng.split("-")
        for rid in range(int(rng_start), int(rng_end) + 1):
            rid_str = str(rid)
            str_len = len(rid_str)
            for size in range(1, str_len // 2 + 1):
                times, rem = divmod(str_len, size)
                if (rem == 0) and (rid_str[:size] * (times) == rid_str):
                    result += rid
                    break

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
