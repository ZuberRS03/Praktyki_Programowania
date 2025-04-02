import os
import random
from asyncio import wait_for
import time

# time.sleep(1)
# os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # grid size
    col = 20
    row = 20

    # create grid
    grid = Grid(col, row)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(grid)
        grid.update()
        time.sleep(1)



class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def __str__(self):
        return str(self.alive)

class Grid:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.grid = [[Cell(random.choice([True, False])) for _ in range(col)] for _ in range(row)]

    def __str__(self):
        grid_str = ""
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j].alive:
                    grid_str += " O"
                else:
                    grid_str += "  "
            grid_str += "\n"
        return grid_str

    def set_cell(self, col, row, alive):
        if 0 <= col < self.col and 0 <= row < self.row:
            self.grid[row][col].alive = alive
        else:
            raise IndexError("Cell coordinates out of bounds")

    def get_cell(self, col, row):
        if 0 <= col < self.col and 0 <= row < self.row:
            return self.grid[row][col].alive
        else:
            raise IndexError("Cell coordinates out of bounds")

    def update(self):
        new_grid = [[Cell() for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                alive_neighbors = self.count_alive_neighbors(i, j)
                if self.grid[i][j].alive:
                    new_grid[i][j].alive = alive_neighbors in (2, 3)
                else:
                    new_grid[i][j].alive = alive_neighbors == 3
        self.grid = new_grid

    def count_alive_neighbors(self, i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        count = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.row and 0 <= nj < self.col and self.grid[ni][nj].alive:
                count += 1
        return count


main()