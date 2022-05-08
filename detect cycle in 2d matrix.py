class Solution:
    def dfs(self, grid, row, col, visit, prev_row, prev_col, prev, visited):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != prev:
            return
        if (row, col) in visit:
            # print(row, col)
            self.ans = True
            return
        # print(row, col, prev_row, prev_col)
        visit.add((row, col))
        visited[row][col] = True
        if row - 1 != prev_row:
            self.dfs(grid, row - 1, col, visit, row, col, grid[row][col], visited)
        if col - 1 != prev_col:
            self.dfs(grid, row, col - 1, visit, row, col, grid[row][col], visited)
        if row + 1 != prev_row:
            self.dfs(grid, row + 1, col, visit, row, col, grid[row][col], visited)
        if col + 1 != prev_col:
            self.dfs(grid, row, col + 1, visit, row, col, grid[row][col], visited)
        visit.remove((row, col))

    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.ans = False
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False:
                    self.ans = False
                    visit = set()
                    self.dfs(grid, i, j, visit, -1, -1, grid[i][j], visited)
                    if self.ans == True:
                        return True
        return False
