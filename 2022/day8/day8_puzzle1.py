import numpy as np

with open("day8_input.txt", encoding="utf-8") as f:
    matrix = np.array([list(row.strip()) for row in f], int)

tree_count = np.zeros_like(matrix, int)

for edge in range(4):
    for h, v in np.ndindex(matrix.shape):
        shorter = [tree < matrix[h, v] for tree in matrix[h, v+1:]]

        tree_count[h, v] |= all(shorter)

    matrix, tree_count = map(np.rot90, [matrix, tree_count])

print(tree_count.sum())
