class Solution:
    def maxDistance(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append([i, j])

        ans = 0
        while q:
            num = len(q)
            for i in range(num):
                x, y = q[0]
                q.pop(0)
                if x > 0 and grid[x - 1][y] == 0:
                    grid[x - 1][y] = 1
                    q.append([x - 1, y])
                if y > 0 and grid[x][y - 1] == 0:
                    grid[x][y - 1] = 1
                    q.append([x, y - 1])
                if x < m - 1 and grid[x + 1][y] == 0:
                    grid[x + 1][y] = 1
                    q.append([x + 1, y])
                if y < n - 1 and grid[x][y + 1] == 0:
                    grid[x][y + 1] = 1
                    q.append([x, y + 1])
            if q: ans += 1

        return -1 if ans == 0 else ans
