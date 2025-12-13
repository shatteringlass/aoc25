from functools import cache


DAY = 11
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False


def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small_2' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines

def parse_line(line):
    src, dst = line.split(':')
    return {src: [d.strip() for d in dst.split()]}

def count_paths(edges, start, end, midpoints={}):

    @cache
    def _navigate(src, seen=frozenset()):
        if src == end:
            return frozenset(midpoints).issubset(seen)
        if src in midpoints:
            seen |= {src}
        return sum(
            _navigate(src=nxt, seen=seen) 
            for nxt in edges[src]
        )
    
    return _navigate(start, frozenset())

def part_one(lines):

    edges = {}
    for line in lines:
        edges.update(parse_line(line))

    return count_paths(edges, 'you', 'out')


def part_two(lines):
    edges = {}
    for line in lines:
        edges.update(parse_line(line))

    return count_paths(edges, 'svr', 'out', {'fft', 'dac'})


def main():
    lines = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(lines)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(lines)}")


if __name__ == "__main__":
    main()
