class Solution:
    def dfs(self, graph, row, col):
        if row < 0 or col < 0 or row == len(graph) or col == len(graph[0]) or graph[row][col] != 'O':
            return
        graph[row][col] = 1
        self.dfs(graph, row - 1, col)
        self.dfs(graph, row, col - 1)
        self.dfs(graph, row + 1, col)
        self.dfs(graph, row, col + 1)

    def solve(self, graph) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(graph), len(graph[0])
        for i in range(m):
            if graph[i][0] == 'O':
                self.dfs(graph, i, 0)
            if graph[i][n - 1] == 'O':
                self.dfs(graph, i, n - 1)

        for i in range(n):
            if graph[0][i] == 'O':
                self.dfs(graph, 0, i)
            if graph[m - 1][i] == 'O':
                self.dfs(graph, m - 1, i)

        for i in range(m):
            for j in range(n):
                if graph[i][j] == 1:
                    graph[i][j] = 'O'
                elif graph[i][j] == 'O':
                    graph[i][j] = 'X'
