class Solution:
    def check(self, grid, row, col):
        if abs(grid[row - 1][col]) == abs(grid[row][col]) and abs(grid[row][col - 1]) == abs(grid[row][col]) and abs(
                grid[row + 1][col]) == abs(grid[row][col]) and abs(grid[row][col + 1]) == abs(grid[row][col]):
            return True
        return False

    def dfs(self, grid, row, col, visited, val):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or visited[row][col] == True or grid[row][
            col] != abs(val):
            return
        if 0 < row < len(grid) - 1 and 0 < col < len(grid[0]) - 1 and self.check(grid, row, col):
            # print(row, col)
            grid[row][col] = grid[row][col]
        else:
            # print(grid[row][col])
            grid[row][col] = -grid[row][col]
        visited[row][col] = True
        self.dfs(grid, row - 1, col, visited, grid[row][col])
        self.dfs(grid, row, col - 1, visited, grid[row][col])
        self.dfs(grid, row + 1, col, visited, grid[row][col])
        self.dfs(grid, row, col + 1, visited, grid[row][col])
        visited[row][col] = False

    def colorBorder(self, grid, row: int, col: int, color: int):
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        self.dfs(grid, row, col, visited, grid[row][col])
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    grid[i][j] = color
        return grid
