highest_total: int = 0
cumulative_total: int = 0

with open("day1_input.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line != "\n":
            cumulative_total += int(line)
        else:
            highest_total = max(cumulative_total, highest_total)
            cumulative_total = 0

print(highest_total)
