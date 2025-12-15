from itertools import chain, combinations, pairwise


DAY = 9
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False

class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Shape:

    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def __init__(self, p1: Point, p2: Point):
        self.x_min, self.x_max = sorted((p1.x,p2.x))
        self.y_min, self.y_max = sorted((p1.y,p2.y))

    
    def is_overlapping(self, other: "Shape"):
        return not(
            (self.x_max <= other.x_min or self.y_max <= other.y_min) # ends before the other starts
            or 
            (self.x_min >= other.x_max or self.y_min >= other.y_max) # starts after the other ends
    )

    def size(self):
        return (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1)


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
    tiles = [Point(*(int(coord) for coord in line.strip().split(","))) for line in lines]
    edges = [Shape(a,b) for a,b in chain(pairwise(tiles), [(tiles[-1], tiles[0])])]
    boxes = [Shape(a,b) for a,b in combinations(tiles, 2)]
    good = [box for box in boxes if not any(box.is_overlapping(edge) for edge in edges)]

    return max(box.size() for box in good)


def main():
    lines = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(lines)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(lines)}")


if __name__ == "__main__":
    main()
