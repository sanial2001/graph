class Solution:
    def dfs(self, graph, row, col, visited, val, diff):
        if row < 0 or col < 0 or row == len(graph) or col == len(graph[0]) or visited[row][col] == True or abs(
                graph[row][col] - val) > diff:
            return
        if row == len(graph) - 1 and col == len(graph[0]) - 1:
            self.check = True
            return
        visited[row][col] = True
        self.dfs(graph, row - 1, col, visited, graph[row][col], diff)
        self.dfs(graph, row, col - 1, visited, graph[row][col], diff)
        self.dfs(graph, row + 1, col, visited, graph[row][col], diff)
        self.dfs(graph, row, col + 1, visited, graph[row][col], diff)
        visited[row][col] = False

    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        start, end = 0, max([max(height) for height in heights])
        self.check, ans = False, -1
        visited = [[False for _ in range(n)] for _ in range(m)]
        while start <= end:
            mid = (start + end) // 2
            self.check = False
            self.dfs(heights, 0, 0, visited, heights[0][0], mid)
            # print(mid, self.check)
            if self.check == True:
                ans = mid
                end = mid - 1
            else:
                start = start + 1

        return ans
