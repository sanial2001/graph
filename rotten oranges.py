class Solution:
    def orangesRotting(self, grid) -> int:
        row, col = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        while q:
            num = len(q)
            for i in range(num):
                x, y = q[0]
                q.pop(0)
                if x > 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    fresh = fresh - 1
                    q.append([x - 1, y])
                if y > 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    fresh = fresh - 1
                    q.append([x, y - 1])
                if x < row - 1 and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    fresh = fresh - 1
                    q.append([x + 1, y])
                if y < col - 1 and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    fresh = fresh - 1
                    q.append([x, y + 1])
            if q: time = time + 1

        return time if fresh == 0 else -1
