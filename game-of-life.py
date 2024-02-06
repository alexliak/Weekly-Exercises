# Import required libraries
import random  # Import the random module for generating random numbers
import pygame  # Import the pygame library for creating a graphical interface

# Initialize Pygame and set up the display
pygame.init()  # Initialize the pygame library

# Define the screen dimensions and size of cells
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Set the dimensions of the window
CELL_SIZE = 20  # Define the size of each cell in pixels
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE  # Calculate the grid dimensions

# Define colors
BACKGROUND_COLOR = (0, 0, 0)  # Define the background color as black (RGB)
REGULAR_CELL_COLOR = (255, 255, 0)  # Define the color for regular cells as yellow (RGB)
AI_CELL_COLOR = (255, 0, 0)  # Define the color for AI cells as red (RGB)

# Create the Pygame screen with the specified dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game of Life with AI")  # Set the window title

# Function to initialize the grid with random cells
def initialize_grid():
    # Create a 2D list filled with random 0s and 1s (representing dead and alive cells)
    return [[random.randint(0, 1) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Function to add more AI cells to the grid
def add_ai_cells(grid, num_ai_cells=5):
    for _ in range(num_ai_cells):
        # Randomly select coordinates and set the cell as an AI cell (value 2)
        x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
        grid[y][x] = 2  # 2 represents an AI cell

# Function to count the number of neighbors for a given cell
def count_neighbors(grid, x, y):
    return sum(
        grid[(y + dy) % GRID_HEIGHT][(x + dx) % GRID_WIDTH]  # Wrap around the grid edges using modulo
        for dy in [-1, 0, 1] for dx in [-1, 0, 1]  # Iterate through neighboring cells
        if (dx, dy) != (0, 0) and grid[(y + dy) % GRID_HEIGHT][(x + dx) % GRID_WIDTH] > 0
        # Exclude the cell itself and count alive neighbors
    )

# Function to determine the best move for an AI cell to maximize survival
def ai_move(grid, x, y):
    best_position = (x, y)  # Initialize the best position as the current position
    max_neighbors = -1  # Initialize the maximum neighbor count
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # Skip the current cell
            # Calculate the new position (wrapping around the grid edges) based on neighbors
            nx, ny = (x + dx) % GRID_WIDTH, (y + dy) % GRID_HEIGHT
            if grid[ny][nx] == 0:  # Check only empty spots
                neighbors = count_neighbors(grid, nx, ny)  # Count neighbors for the potential move
                if 2 <= neighbors <= 3 and neighbors > max_neighbors:
                    best_position = (nx, ny)  # Update best position if conditions are met
                    max_neighbors = neighbors  # Update maximum neighbor count
    return best_position  # Return the best position to move to

# Function to update the grid with AI logic included
def update_grid(grid):
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # Create a new empty grid
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = count_neighbors(grid, x, y)  # Count neighbors for the current cell
            if grid[y][x] == 2:  # Check if it's an AI cell
                nx, ny = ai_move(grid, x, y)  # Determine the best move for the AI cell
                new_grid[ny][nx] = 2  # Update the new grid with the AI cell in the new position
            elif grid[y][x] == 1 and 2 <= neighbors <= 3:
                new_grid[y][x] = 1  # Regular cell survives based on neighbor count
            elif grid[y][x] == 0 and neighbors == 3:
                new_grid[y][x] = 1  # A new cell is born if there are exactly 3 neighbors
    return new_grid  # Return the updated grid

# Function to draw the grid on the Pygame screen
def draw_grid(grid):
    screen.fill(BACKGROUND_COLOR)  # Fill the screen with the background color
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 1:
                color = REGULAR_CELL_COLOR  # Set the color for regular cells
            elif grid[row][col] == 2:
                color = AI_CELL_COLOR  # Set the color for AI cells
            else:
                continue  # Skip drawing for empty cells
            # Draw a rectangle representing the cell with the appropriate color and size
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main game loop
grid = initialize_grid()  # Initialize the grid with random cells
add_ai_cells(grid, num_ai_cells=680)  # Add 750 red AI cells to the grid

running = True  # Set the game loop condition to True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # If the window is closed, exit the game loop
    
    grid = update_grid(grid)  # Update the grid for the next generation
    draw_grid(grid)  # Draw the updated grid on the screen
    pygame.display.flip()  # Update the display to show the latest grid state
    pygame.time.delay(100)  # Slow down the simulation by delaying for 100 milliseconds

# Quit Pygame when the game loop ends
pygame.quit()
