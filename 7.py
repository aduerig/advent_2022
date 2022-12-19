from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


class directory():
    def __init__(self, path):
        self.path = path
        self.children = set()
        self.size_of_files = 0

    def __hash__(self):
        return hash(self.path)

    def __eq__(self, o):
        return self.path == o.path

    def __repr__(self):
        return f'/{self.path}: {self.size_of_files}'        


curr = []
root_dir = directory('')
last_directory = root_dir
directories = {'': root_dir}
with open(data_file) as f:
    f.readline()
    for line in f.readlines():
        line = line.strip()
        if line.startswith('$'):
            line = line[2:]
            if line != 'ls':
                _, dir_name = line.split()
                if '/' in dir_name:
                    print(dir_name)
                    exit()
                if dir_name == '..':
                    if len(curr):
                        curr.pop()
                else:
                    curr.append(dir_name)
                path_gone_to = '/'.join(curr)
                if path_gone_to not in directories:
                    directories[path_gone_to] = directory(path_gone_to)
                last_directory = directories[path_gone_to]
            print(directories)

        else:
            first, second = line.split()
            if '/' in second:
                print('nah')
                exit()
            if first == 'dir':
                if curr:
                    path_found = '/'.join(curr) + '/' + second
                else:
                    path_found = second
                if path_found not in directories:
                    directories[path_found] = directory(path_found)
                sub_dir = directories[path_found]
                if sub_dir not in last_directory.children:
                    last_directory.children.add(sub_dir)
            else:
                last_directory.size_of_files += int(first)


seen = {}
def dfs(node):
    if node in seen:
        return seen[node]
    total = node.size_of_files
    print_yellow('dfs', node, total)
    for child in node.children:
        total += dfs(child)
    seen[node] = total
    return total
needed = 30000000 - (70000000 - dfs(root_dir))

print(seen)
revved = map(lambda x: list(reversed(x)), seen.items())
the_sort = sorted(revved, key=lambda x: x[0])
print(the_sort)
for amt, directory in the_sort:
    print(amt, directory)
    if amt >= needed:
        print_green(dfs(directory))
        break

print_cyan('needed', needed)

# too high
# 27924493
# 24933642