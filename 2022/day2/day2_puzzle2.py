total_score: int = 0

scores = {
    ('A', 'X'): 3,
    ('B', 'X'): 1,
    ('C', 'X'): 2,
    ('A', 'Y'): 4,
    ('B', 'Y'): 5,
    ('C', 'Y'): 6,
    ('A', 'Z'): 8,
    ('B', 'Z'): 9,
    ('C', 'Z'): 7,
}

with open("day2_input.txt", encoding="utf-8") as f:
    for line in f.readlines():
        t = tuple(line.split())
        total_score += scores[t]

print(total_score)
