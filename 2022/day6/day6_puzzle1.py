from collections import deque

char_buffer = deque(maxlen=4)

with open("day6_input.txt", encoding="utf-8") as f:
    line = f.readline()
    for i, c in enumerate(line):
        if len(char_buffer) <= 3:
            char_buffer.append(c)
            continue

        char_buffer.append(c)
        duplicates = [char_buffer.count(x) for x in char_buffer]

        if sum(duplicates) == 4:
            print(i+1)
            break
