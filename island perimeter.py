class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 4
                    ans -= grid[i - 1][j] if i > 0 else 0
                    ans -= grid[i + 1][j] if i < m - 1 else 0
                    ans -= grid[i][j - 1] if j > 0 else 0
                    ans -= grid[i][j + 1] if j < n - 1 else 0
        return ans
