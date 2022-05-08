class Solution:
    def dfs(self, board, row, col):
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] != 'X':
            return
        board[row][col] = 'O'
        self.dfs(board, row + 1, col)
        self.dfs(board, row, col + 1)

    def countBattleships(self, board) -> int:
        ans = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    ans += 1
                    self.dfs(board, i, j)
        return ans
