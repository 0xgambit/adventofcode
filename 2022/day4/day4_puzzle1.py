count_pairs: int = 0

with open("day4_input.txt", encoding="utf-8") as f:
    for line in f.readlines():
        pair1, pair2 = line.split(',')
        start1, end1 = pair1.split('-')
        start2, end2 = pair2.split('-')
        start1, start2, end1, end2 = [int(x) for x in [start1, start2, end1, end2]]
        if (start1 <= start2 and end2 <= end1) \
                or (start2 <= start1 and end1 <= end2):
            count_pairs += 1

print(count_pairs)
