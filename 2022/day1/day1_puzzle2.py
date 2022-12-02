array_totals: list = []
cumulative_total: int = 0

with open("day1_input.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line != "\n":
            cumulative_total += int(line)
        else:
            array_totals.append(cumulative_total)
            cumulative_total = 0

array_totals.sort()
print(sum(array_totals[-3:]))
