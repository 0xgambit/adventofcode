total_score: int = 0

scores = {
    ('A', 'X'): 4,
    ('B', 'X'): 1,
    ('C', 'X'): 7,
    ('A', 'Y'): 8,
    ('B', 'Y'): 5,
    ('C', 'Y'): 2,
    ('A', 'Z'): 3,
    ('B', 'Z'): 9,
    ('C', 'Z'): 6,
}

with open("day2_input.txt", encoding="utf-8") as f:
    for line in f.readlines():
        t = tuple(line.split())
        total_score += scores[t]

print(total_score)
