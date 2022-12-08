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
        for child in self.dirs:
            if child.name == name:
                return child
        return None

    def has_children(self):
        return len(self.dirs) > 0
    
    def size(self):
        size = 0
        for file in self.files:
            size += file["size"]
        for dir in self.dirs:
            size += dir.size()
        return size
    
    def pretty_dir(self, indent=2):
        sol = ""
        for file in self.files:
            sol += " " * indent + "- " + file["name"] + " (file, size=" + (str(file["size"])) + ")\n"
        for dir in self.dirs:
            sol += " " * indent + "- " + dir.name + f" (dir, size={dir.size()})\n"
            sol += dir.pretty_dir(indent + 2)
        return sol
    
    def pretty(self):
        sol = "- " + self.name + f" (dir, size={self.size()})\n"
        sol += self.pretty_dir()
        return sol

    def __repr__(self):
        return str({"name": self.name, "dirs": self.dirs, "files": self.files})


def extract_tree(data=read_data()[1:]):
    tree = Node("/")
    current = tree
    for line in data:
        tokens = line.split(" ")
        if tokens[1] == "ls":
            continue
        if tokens[0] == "$":
            if tokens[1] == "cd":
                dir_name = tokens[2]
                if dir_name == "..":
                    current = current.parent
                else:
                    current = current.fetch_child(dir_name)

        if tokens[0] == "dir":
            dir_name = tokens[1]
            if current.fetch_child(dir_name) is None:
                current.add_dir(dir_name)

        if tokens[0].isdigit():
            current.add_file(tokens[1], int(tokens[0]))
    return tree

tree = extract_tree()

def get_directory_sizes():
    sizes = []
    def get_sizes(node):
        if node.has_children():
            for child in node.dirs:
                get_sizes(child)
        sizes.append(node.size())
    get_sizes(tree)
    return sizes

def find_elibile_dirs(size_to_delete):
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
    threshold = 100000
    sizes = get_directory_sizes()
    within = [size for size in sizes if threshold > size]
    print(f"Part1: {sum([size for size in within])}")

def part2():
    available = 70000000
    need = 30000000
    total_size = tree.size()
    left = available - total_size
    size_to_delete = need - left
    dirs = find_elibile_dirs(size_to_delete)
    sizes = [dir.size() for dir in dirs]
    sizes.sort()
    print(f"Part2: {sizes[0]}")

if __name__ == '__main__':
    part1()
    part2()
