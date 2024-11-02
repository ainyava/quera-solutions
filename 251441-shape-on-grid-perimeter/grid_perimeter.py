n = int(input())

grid_rows = n + 2
grid_columns = 102
grid = [[0] * grid_columns for _ in range(grid_rows)]

for row in range(1, n + 1):
    l, r = map(int, input().split())
    for col in range(l, r):
        grid[row][col] = 1

perimeter = 0

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if grid[i][j] == 1:
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if grid[ni][nj] == 0:
                    perimeter += 1

print(perimeter)
