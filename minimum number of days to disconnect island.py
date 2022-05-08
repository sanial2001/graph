class Solution:
    def dfs(self, grid, row, col, visit):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or (row, col) in visit or grid[row][col] != 1:
            return
        visit.add((row, col))
        self.dfs(grid, row - 1, col, visit)
        self.dfs(grid, row, col - 1, visit)
        self.dfs(grid, row + 1, col, visit)
        self.dfs(grid, row, col + 1, visit)

    def count(self, grid):
        m, n = len(grid), len(grid[0])
        visit = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visit:
                    ans += 1
                    self.dfs(grid, i, j, visit)
        # print(ans)
        return ans

    def minDays(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        if self.count(grid) != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.count(grid) != 1:
                        return 1
                    grid[i][j] = 1

        return 2
