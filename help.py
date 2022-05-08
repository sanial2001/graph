class Solution:
        def dfs(self, board, row, col, word, i, visited):
            if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or visited[row][col] == True or board[row][col] != word[i]:
                return
            if i == len(word) - 1 and board[row][col] == word[i]:
                self.ans = True
                return
            visited[row][col] = True
            self.dfs(board, row - 1, col, word, i + 1, visited)
            self.dfs(board, row, col - 1, word, i + 1, visited)
            self.dfs(board, row + 1, col, word, i + 1, visited)
            self.dfs(board, row, col + 1, word, i + 1, visited)
            visited[row][col] = False

        def isWordExist(self, board, word):
            # Code here
            self.ans = False
            m, n = len(board), len(board[0])
            visited = [[False for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        print(word[0])
                        self.dfs(board, i, j, word, 0, visited)
                        if self.ans == True:
                            return True
            return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    print(Solution().isWordExist(board, word))
