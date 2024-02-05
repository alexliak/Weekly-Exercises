import copy
import time
import os

# Initialize the grid
def create_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]  # Added iteration variables

# Display the grid
def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    time.sleep(0.5)

# Count neighbors
def count_neighbors(grid, row, col):
    neighbors = 0
    for i in range(max(0, row-1), min(len(grid), row+2)):
        for j in range(max(0, col-1), min(len(grid[0]), col+2)):
            neighbors += grid[i][j]
    neighbors -= grid[row][col]
    return neighbors

# Update the grid
def update_grid(grid):
    new_grid = copy.deepcopy(grid)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            neighbors = count_neighbors(grid, i, j)
            if cell == 0 and neighbors == 3:
                new_grid[i][j] = 1
            elif cell == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i][j] = 0
    return new_grid

# Main function
def main():
    rows, cols = 10, 10
    grid = create_grid(rows, cols)
    # Initial configuration
    grid[1][2] = grid[2][3] = grid[3][1] = grid[3][2] = grid[3][3] = 1

    while True:
        display_grid(grid)
        grid = update_grid(grid)

if __name__ == "__main__":
    main()
