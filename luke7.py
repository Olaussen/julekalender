import sys
sys.setrecursionlimit(10000)

def read_data():
    with open('./data/luke7.txt') as f:
        return [x.strip() for x in f.readlines()]

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []
    
    def add_dir(self, dir_name):
        self.dirs.append(Node(dir_name, self))

    def add_file(self, name, size):
        self.files.append({"name": name, "size": size})

    def is_child(self, node):
        return node.parent == self

    def fetch_child(self, name):
        return next((child for child in self.dirs if child.name == name), None)

    def has_children(self):
        return len(self.dirs) > 0
    
    def size(self):
        return sum([file["size"] for file in self.files]) + sum([dir.size() for dir in self.dirs])

def extract_tree(data=read_data()[1:]):
    tree = Node("/")
    current = tree
    for line in data:
        tokens = line.split(" ")
        if tokens[0] == "$" and tokens[1] == "cd":
            current = current.parent if tokens[2] == ".." else current.fetch_child(tokens[2])
        if tokens[0] == "dir" and current.fetch_child(tokens[1]) is None:
            current.add_dir(tokens[1])
        if tokens[0].isdigit():
            current.add_file(tokens[1], int(tokens[0]))
    return tree


def get_directory_sizes(tree):
    sizes = []
    def get_sizes(node):
        if node.has_children():
            for child in node.dirs:
                get_sizes(child)
        sizes.append(node.size())
    get_sizes(tree)
    return sizes

def find_elibile_dirs(tree, size_to_delete):
    dirs = []
    def find_eligible(node):
        if node.has_children():
            for child in node.dirs:
                find_eligible(child)
        if node.size() >= size_to_delete:
            dirs.append(node)
    find_eligible(tree)
    return dirs

def part1():
    tree = extract_tree()
    print("Part 1:", {sum([size for size in get_directory_sizes(tree) if 100000 > size])})

def part2():
    tree = extract_tree()
    print("Part 2:", {sorted([dir.size() for dir in find_elibile_dirs(tree, 30000000 - (70000000 - tree.size()))])[0]})

if __name__ == '__main__':
    part1()
    part2()
