import random

LIVE_COLOR = 254
DEAD_COLOR = 0
DEFAULT_LIVE_CELLS = 2048

class Grid:
    def __init__(self, display_width, display_height):
        self.width = display_width
        self.height = display_height
        self.live_cells = {}

    def initialize_random(self):
        initial_live_cells = min(DEFAULT_LIVE_CELLS, self.width * self.height // 4)
        self.randomize_live_cells(initial_live_cells)

    def randomize_live_cells(self, num_live_cells):
        while len(self.live_cells) < num_live_cells:
            row = random.randint(0, self.height - 1)
            col = random.randint(0, self.width - 1)
            self.live_cells[(row, col)] = True

    def initialize_with_patterns(self, patterns):
        for pattern in patterns:
            pattern_height = len(pattern)
            pattern_width = len(pattern[0])
            start_row = random.randint(0, self.height - pattern_height)
            start_col = random.randint(0, self.width - pattern_width)
            for i in range(pattern_height):
                for j in range(pattern_width):
                    if pattern[i][j] == 1:
                        self.live_cells[(start_row + i, start_col + j)] = True

    def display_contents(self, tft):
        tft.fill(0)  # Clear the display
        for cell in self.live_cells:
            tft.pixel(cell[0], cell[1], LIVE_COLOR)

    def count_neighbors(self, cell):
        count = 0
        row, col = cell
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i, j) != cell and self.live_cells.get((i, j)):
                    count += 1
        return count

    def evolve(self):
        new_live_cells = {}
        neighbor_counts = {}

        # Count neighbors for live cells and their immediate neighbors
        for cell in self.live_cells:
            count = self.count_neighbors(cell)
            neighbor_counts[cell] = count
            for i in range(cell[0] - 1, cell[0] + 2):
                for j in range(cell[1] - 1, cell[1] + 2):
                    if (i, j) != cell:
                        neighbor_counts[(i, j)] = neighbor_counts.get((i, j), 0) + 1

        # Apply Game of Life rules to determine new live cells
        for cell, count in neighbor_counts.items():
            if count == 3 or (count == 2 and cell in self.live_cells):
                new_live_cells[cell] = True

        self.live_cells = new_live_cells
