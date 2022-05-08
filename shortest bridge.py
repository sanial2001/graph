class Solution:
    def dfs(self, grid, row, col, q):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 1:
            return
        grid[row][col] = 2
        q.append([row, col])
        self.dfs(grid, row - 1, col, q)
        self.dfs(grid, row, col - 1, q)
        self.dfs(grid, row + 1, col, q)
        self.dfs(grid, row, col + 1, q)

    def check(self, grid, q):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, q)
                    return

    def shortestBridge(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        self.check(grid, q)
        '''
        for val in grid:
            print(val)
        '''
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited[i][j] = True
        ans = -1
        while q:
            num = len(q)
            for i in range(num):
                x, y = q.pop(0)
                # print(grid[x][y], x, y)
                if grid[x][y] == 1:
                    return ans
                if x > 0 and visited[x - 1][y] == False:
                    visited[x - 1][y] = True
                    q.append([x - 1, y])
                if y > 0 and visited[x][y - 1] == False:
                    visited[x][y - 1] = True
                    q.append([x, y - 1])
                if x < m - 1 and visited[x + 1][y] == False:
                    visited[x + 1][y] = True
                    q.append([x + 1, y])
                if y < n - 1 and visited[x][y + 1] == False:
                    visited[x][y + 1] = True
                    q.append([x, y + 1])
            ans += 1
