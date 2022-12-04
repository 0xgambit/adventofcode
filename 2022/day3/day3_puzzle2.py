sum_of_values: int = 0

with open("day3_input.txt", encoding="utf-8") as f:
    for first_line in f:
        second_line, third_line = next(f), next(f)
        common_char = (set(first_line) & set(second_line)) & set(third_line)
        common_char.remove('\n')
        common_char = next(iter(common_char))
        value = ord(common_char) - 38 if common_char.isupper() else ord(common_char) - 96
        sum_of_values += value

print(sum_of_values)
