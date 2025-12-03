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
    max_nums = find_max_seq(lines, 2)
    result = 0

    for bank_seq in max_nums:
        for idx, num in enumerate(bank_seq):
            result += num * 10 ** (1 - idx)

    return result


def part_two(lines):
    max_nums = find_max_seq(lines, 12)
    result = 0

    for bank_seq in max_nums:
        for idx, num in enumerate(bank_seq):
            result += num * 10 ** (11 - idx)

    return result


def find_max_seq(banks, seqlen):
    maxbatt = seqlen
    max_nums = []

    for bank in banks:
        left = 0
        bank = list(map(int, bank.strip()))
        max_nums_bank = []
        for k in range(maxbatt):
            right = len(bank) - (maxbatt - k) + 1
            chunk = bank[left:right]
            curmax = max(chunk)
            max_nums_bank.append(curmax)
            left += chunk.index(curmax) + 1
        max_nums.append(max_nums_bank)

    return max_nums


def main():
    lines = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(lines)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(lines)}")


if __name__ == "__main__":
    main()
