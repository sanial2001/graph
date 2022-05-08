class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 0:
            return
        grid[row][col] = 2
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col + 1)

    def closedIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            if grid[0][i] == 0:
                self.dfs(grid, 0, i)
            if grid[m - 1][i] == 0:
                self.dfs(grid, m - 1, i)
        for i in range(m):
            if grid[i][0] == 0:
                self.dfs(grid, i, 0)
            if grid[i][n - 1] == 0:
                self.dfs(grid, i, n - 1)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    ans += 1
                    self.dfs(grid, i, j)
        return ans
