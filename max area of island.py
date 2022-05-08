class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 1:
            return 0
        grid[row][col] = 2
        x1 = self.dfs(grid, row - 1, col)
        x2 = self.dfs(grid, row, col - 1)
        x3 = self.dfs(grid, row + 1, col)
        x4 = self.dfs(grid, row, col + 1)
        return 1 + x1 + x2 + x3 + x4

    def maxAreaOfIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))
        return ans
