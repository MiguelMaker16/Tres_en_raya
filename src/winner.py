def playerWinner(grid):
    #row_grid
    for row_grid in grid:
        if row_grid[0] == row_grid[1] == row_grid[2] != 0:
            return row_grid[0]
    #col_grid
    for col_grid in range(3):
        if grid[0][col_grid] == grid[1][col_grid] == grid[2][col_grid] != 0:
            return grid[0][col_grid]
    #diagonal
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]
    #tie
    return None