from collections import defaultdict
from itertools import accumulate


directories = defaultdict(int)
dir_limit = 100_000
root_limit = 40_000_000

with open("day7_input.txt", encoding="utf-8") as f:
    for line in f:
        match line.split():
            case '$', 'ls': pass
            case 'dir', _: pass
            case '$', 'cd', '/': current_dir = ['']
            case '$', 'cd', '..': current_dir.pop()
            case '$', 'cd', d: current_dir.append(f'{d}/')
            case size, _:
                for path in accumulate(current_dir):
                    directories[path] += int(size)

print(min(f_size for f_size in directories.values() if f_size >= directories[''] - root_limit))
