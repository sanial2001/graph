class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1
        q = [(0, 0)]
        grid[0][0] = 1
        ans = 1

        while q:
            for i in range(len(q)):
                row, col = q.pop(0)
                if row == m - 1 and col == n - 1:
                    return ans
                if row > 0 and grid[row - 1][col] == 0:
                    grid[row - 1][col] = 1
                    q.append((row - 1, col))
                if row > 0 and col > 0 and grid[row - 1][col - 1] == 0:
                    grid[row - 1][col - 1] = 1
                    q.append((row - 1, col - 1))
                if col > 0 and grid[row][col - 1] == 0:
                    grid[row][col - 1] = 1
                    q.append((row, col - 1))
                if row < m - 1 and col > 0 and grid[row + 1][col - 1] == 0:
                    grid[row + 1][col - 1] = 1
                    q.append((row + 1, col - 1))
                if row < m - 1 and grid[row + 1][col] == 0:
                    grid[row + 1][col] = 1
                    q.append((row + 1, col))
                if row < m - 1 and col < n - 1 and grid[row + 1][col + 1] == 0:
                    grid[row + 1][col + 1] = 1
                    q.append((row + 1, col + 1))
                if col < n - 1 and grid[row][col + 1] == 0:
                    grid[row][col + 1] = 1
                    q.append((row, col + 1))
                if row > 0 and col < n - 1 and grid[row - 1][col + 1] == 0:
                    grid[row - 1][col + 1] = 1
                    q.append((row - 1, col + 1))
            ans += 1

        return -1
