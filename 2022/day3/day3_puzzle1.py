sum_of_values: int = 0

with open("day3_input.txt", encoding="utf-8") as f:
    for line in f.readlines():
        first_half, second_half = line[:len(line)//2], line[len(line)//2:]
        common_char = next(iter(set(first_half) & set(second_half)))
        value = ord(common_char) - 38 if common_char.isupper() else ord(common_char) - 96
        sum_of_values += value

print(sum_of_values)
