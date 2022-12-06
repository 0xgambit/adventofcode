from collections import deque

char_buffer = deque(maxlen=14)

with open("day6_input.txt", encoding="utf-8") as f:
    line = f.readline()
    for i, c in enumerate(line):
        if len(char_buffer) <= 13:
            char_buffer.append(c)
            continue

        char_buffer.append(c)
        duplicates = [char_buffer.count(x) for x in char_buffer]

        if sum(duplicates) == 14:
            print(i+1)
            break
