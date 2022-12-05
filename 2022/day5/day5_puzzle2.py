from collections import defaultdict

crates = defaultdict(list)

with open("day5_input.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line.startswith(' 1') or line == '\n':
            continue
        if line.startswith('move'):
            instruction = line.split()
            from_stack = int(instruction[3])
            to_stack = int(instruction[5])
            no_crates = int(instruction[1])
            crates_to_move = crates[from_stack][:no_crates]
            # crates_to_move.reverse()
            crates[to_stack] = crates_to_move + crates[to_stack]
            del crates[from_stack][:no_crates]
            continue

        row = [line[i:i+4].strip() for i in range(0, len(line), 4)]
        [crates[count+1].append(crate) for count, crate in enumerate(row) if crate != '']

print((''.join([crates[i][0] for i in range(1, 10)])).replace('[', '').replace(']', ''))
