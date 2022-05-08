class Solution:
    def pacific(self, graph, row, col, val, visit):
        if row < 0 or col < 0 or row == len(graph) or col == len(graph[0]) or graph[row][col] > val or visit[row][
            col] == True:
            if row < 0 or col < 0:
                self.temp = 1
            return
        visit[row][col] = True
        self.pacific(graph, row - 1, col, graph[row][col], visit)
        self.pacific(graph, row, col - 1, graph[row][col], visit)
        self.pacific(graph, row + 1, col, graph[row][col], visit)
        self.pacific(graph, row, col + 1, graph[row][col], visit)
        visit[row][col] = False

    def atlantic(self, graph, row, col, val, visit):
        if row == len(graph) or col == len(graph[0]) or row < 0 or col < 0 or graph[row][col] > val or visit[row][
            col] == True:
            if row == len(graph) or col == len(graph[0]):
                self.temp = 1
            return
        visit[row][col] = True
        self.atlantic(graph, row - 1, col, graph[row][col], visit)
        self.atlantic(graph, row, col - 1, graph[row][col], visit)
        self.atlantic(graph, row + 1, col, graph[row][col], visit)
        self.atlantic(graph, row, col + 1, graph[row][col], visit)
        visit[row][col] = False

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[0 for _ in range(n)] for _ in range(m)]
        bool_pac = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[0 for _ in range(n)] for _ in range(m)]
        bool_atl = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.temp = 0
                self.pacific(heights, i, j, 100000000, bool_pac)
                pacific[i][j] = self.temp

        for i in range(m):
            for j in range(n):
                self.temp = 0
                self.atlantic(heights, i, j, 100000000, bool_atl)
                atlantic[i][j] = self.temp

        '''
        for val in pacific:
            print(val)
        print('\n')
        for val in atlantic:
            print(val)
        '''
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    ans.append([i, j])

        return ans
