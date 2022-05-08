class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 1:
            return 0
        grid[row][col] = 2
        x1 = self.dfs(grid, row - 1, col)
        x2 = self.dfs(grid, row - 1, col - 1)
        x3 = self.dfs(grid, row, col - 1)
        x4 = self.dfs(grid, row + 1, col - 1)
        x5 = self.dfs(grid, row + 1, col)
        x6 = self.dfs(grid, row + 1, col + 1)
        x7 = self.dfs(grid, row, col + 1)
        x8 = self.dfs(grid, row - 1, col + 1)
        return 1 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8

        # Function to find unit area of the largest region of 1s.

    def findMaxArea(self, grid):
        # Code here
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))
        return ans
