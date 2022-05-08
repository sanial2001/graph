class Solution:
    def dfs(self, land, row, col):
        if row < 0 or col < 0 or row == len(land) or col == len(land[0]) or land[row][col] != 1:
            return
        land[row][col] = 2
        self.r2, self.c2 = max(self.r2, row), max(self.c2, col)
        self.dfs(land, row - 1, col)
        self.dfs(land, row, col - 1)
        self.dfs(land, row + 1, col)
        self.dfs(land, row, col + 1)

    def findFarmland(self, land):
        m, n = len(land), len(land[0])
        ans = []
        self.r2, self.c2 = 0, 0
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    self.r2, self.c2 = 0, 0
                    self.dfs(land, i, j)
                    ans.append([i, j, self.r2, self.c2])
        return ans
