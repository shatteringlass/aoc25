DAY = 3
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False


def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines


def part_one(lines):
    result = sum(
        int("".join(map(str, find_max_seq(bank=line, seqlen=2)))) for line in lines
    )
    return result


def part_two(lines):
    result = sum(
        int("".join(map(str, find_max_seq(bank=line, seqlen=12)))) for line in lines
    )
    return result


def find_max_seq(bank, seqlen):
    left = 0
    bank = list(map(int, bank.strip()))
    max_nums_bank = []
    for k in range(seqlen):
        right = len(bank) - (seqlen - k) + 1
        chunk = bank[left:right]
        curmax = max(chunk)
        max_nums_bank.append(curmax)
        left += chunk.index(curmax) + 1
    return max_nums_bank


def main():
    lines = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(lines)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(lines)}")


if __name__ == "__main__":
    main()
