# original
def kill_count(tree_map: list, slope: int) -> int:
    """
    Given an imported tree_map list
    calculate number of deaths by hitting a tree
    """
    # when we reach the wrap point
    # go back to the front + diff of wrap
    # len(tree_map[0])
    wrap = len(tree_map[0].strip())
    position = 0
    deaths = 0
    for line in tree_map:
        print("NEW TREE LINE")
        print("*"*31)
        line = line.strip()
        print(line)
        print(position)
        print(len(line))
        if position >= len(line):
            position = position - wrap
        print(line[position])
        if line[position] == "#":
            deaths += 1
        position += slope
        print(deaths)
    return deaths

# part 2
def kill_count(tree_map, slope, skip=0) -> int:
    """
    Given an imported tree_map list
    calculate number of deaths by hitting a tree
    optional line skips
    """
    # when we reach the wrap point
    # go back to the front + diff of wrap
    # len(tree_map[0])
    wrap = len(tree_map[0].strip())
    position = 0
    deaths = 0
    index = 0
    while index < len(tree_map):
        line = tree_map[index].strip()
        print("NEW TREE LINE")
        print("*"*wrap)
        print(line)
        print(position)
        print(len(line))
        if position >= len(line):
            position = position - wrap
        print(line[position])
        if line[position] == "#":
            deaths += 1
        position += slope
        print(deaths)
        index += 1 + skip
    return deaths


# I imported something...was trying hard not to, but i like reduce
from functools import reduce


def check_tree_algo(tree_map: list, rules: tuple) -> int:
    """
    check multiple rules given a tree_map and multiply their returns
    rules are tuples of ints
    rule[0] = right move
    rule[1] = down move
    """
    kill_counts =  []
    for rule in rules:
        print("%"*len(tree_map[0]))
        print("Beginning new rule set")
        print(f"rules is right {rule[0]}, down {rule[1]}")
        kill_counts.append(kill_count(tree_map, rule[0], skip=rule[1]-1))
    return reduce(lambda x, y: x*y, kill_counts)


rule_map = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
