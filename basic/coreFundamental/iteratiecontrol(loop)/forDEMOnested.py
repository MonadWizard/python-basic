"""
for variable in sequence:
    action
"""

num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print("[2][2]",num_grid[2][2])

for row in num_grid:
    for col in row:
        print(col)