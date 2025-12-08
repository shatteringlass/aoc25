
import dataclasses
import math


DAY = 8
PARTS = (1, 2)
INPUT_FOLDER = "inputs"
TEST_SMALL = False

@dataclasses.dataclass
class Node:
    x: int
    y: int
    z: int

    def distance(self, other: "Node") -> float:
        return math.pow(
            math.pow(self.x - other.x, 2) 
            + math.pow(self.y - other.y, 2) 
            + math.pow(self.z - other.z, 2),
            0.5
        )

    @property
    def coords(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)
    
@dataclasses.dataclass
class Network:
    nodes: list[Node]
    distances: dict[tuple[tuple[int,int,int]], float] = dataclasses.field(init=False)

    def __post_init__(self):
        dist = dict()
        for nidx in range(len(self.nodes)):
            for midx in range(len(self.nodes) - 1, -1, -1):
                if nidx == midx:
                    break
                else:
                    dist[tuple((nidx, midx))] = self.nodes[nidx].distance(self.nodes[midx])
        self.distances = dict(sorted(dist.items(), key=lambda item: item[1]))

    def find_closest_pair(self):
        # return the two nodes with the smallest distance
        closest = next(iter(self.distances))
        return closest, self.distances.pop(closest)


def parse_input(small=TEST_SMALL):
    filename = INPUT_FOLDER + f"/{DAY:02d}{'_small' if small else ''}.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    return lines


def part_one(lines):
    result = 1
    nodes = []

    for line in lines:
        x, y, z = line.split(',')
        nodes.append(Node(int(x), int(y), int(z)))
    
    network = Network(nodes=nodes)

    circuits = {idx: set({idx}) for idx in range(len(network.nodes))}
    pairs = 0

    while pairs < 1000:
        if not network.distances:
            break
        (lid, rid), _ = network.find_closest_pair()
        for box in (circuits[lid] | circuits[rid]):
            circuits[box] |= (circuits[lid] | circuits[rid])
        pairs += 1
    
    unique_circuits = set({frozenset(v) for v in circuits.values()})
    for size in sorted([len(x) for x in unique_circuits], reverse=True)[:3]:
        result *= size
    return result




def part_two(lines):
    result = 1
    nodes = []

    for line in lines:
        x, y, z = line.split(',')
        nodes.append(Node(int(x), int(y), int(z)))
    
    network = Network(nodes=nodes)

    circuits = {idx: set({idx}) for idx in range(len(network.nodes))}

    while True:
        if len(circuits[0]) == len(network.nodes):
            break
        (lid, rid), _ = network.find_closest_pair()
        for box in (circuits[lid] | circuits[rid]):
            circuits[box] |= (circuits[lid] | circuits[rid])
    
    result *= network.nodes[lid].x * network.nodes[rid].x
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
