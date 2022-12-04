def cavityMap(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i != 0 and i != len(grid) - 1 and j != 0 and j != len(grid) - 1 or j != 0 and j != len(grid) - 1 and i != 0 and i != len(grid) - 1:
                if grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i][j-1]: 
                    val = list(grid[i])
                    val[j] = 'X'
                    grid[i] = "".join(val)
    return grid
