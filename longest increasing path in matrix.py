class Solution:
    def dfs(self, matrix, row, col, val, ans):
        if row < 0 or col < 0 or row == len(matrix) or col == len(matrix[0]) or matrix[row][col] <= val:
            return 0
        if (row, col) in ans:
            return ans[(row, col)]
        ans[(row, col)] = max(1 + self.dfs(matrix, row - 1, col, matrix[row][col], ans),
                              1 + self.dfs(matrix, row, col - 1, matrix[row][col], ans),
                              1 + self.dfs(matrix, row + 1, col, matrix[row][col], ans),
                              1 + self.dfs(matrix, row, col + 1, matrix[row][col], ans))
        return ans[(row, col)]

    def longestIncreasingPath(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = {}
        for i in range(m):
            for j in range(n):
                ans[(i, j)] = self.dfs(matrix, i, j, -1, ans)
        return max(ans.values())
