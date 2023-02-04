class Solution:
    def dfs_down(self, grid, i, j):
        if i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
            return False
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return True
        if i == 0 and j == 0:
            grid[i][j] = 1
        else:
            grid[i][j] = 0
        return self.dfs_down(grid, i + 1, j) or self.dfs_down(grid, i, j + 1)

    def dfs_up(self, grid, i, j):
        if i < 0 or j < 0 or grid[i][j] == 0:
            return False
        if i == 0 and j == 0:
            return True
        return self.dfs_up(grid, i - 1, j) or self.dfs_up(grid, i, j - 1)

    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        temp = self.dfs_down(grid, 0, 0)
        '''
        for val in grid:
            print(val)
        '''
        if temp == False:
            return True
        else:
            return False if self.dfs_up(grid, m - 1, n - 1) else True
