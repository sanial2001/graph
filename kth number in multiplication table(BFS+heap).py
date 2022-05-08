import heapq

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        visited = [[False for _ in range(n)] for _ in range(m)]
        t = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                t[i][j] = (i + 1) * (j + 1)
        pq = [(t[0][0], 0, 0)]
        k = k - 1
        while pq:
            ele, x, y = heapq.heappop(pq)
            if k == 0:
                return ele
            visited[x][y] = True
            if x < m - 1 and visited[x + 1][y] == False:
                visited[x + 1][y] = True
                heapq.heappush(pq, (t[x + 1][y], x + 1, y))
            if y < n - 1 and visited[x][y + 1] == False:
                visited[x][y + 1] = True
                heapq.heappush(pq, (t[x][y + 1], x, y + 1))
            k = k - 1
