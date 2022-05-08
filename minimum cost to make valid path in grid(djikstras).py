import heapq


class Solution:
    def minCost(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(0, 0, 0)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        while pq:
            cost, x, y = heapq.heappop(pq)
            # print(cost, x, y)
            visited[x][y] = True
            if x == m - 1 and y == n - 1:
                return cost
            if x > 0 and visited[x - 1][y] == False:
                if grid[x][y] == 4:
                    heapq.heappush(pq, (cost, x - 1, y))
                else:
                    heapq.heappush(pq, (cost + 1, x - 1, y))
            if y > 0 and visited[x][y - 1] == False:
                if grid[x][y] == 2:
                    heapq.heappush(pq, (cost, x, y - 1))
                else:
                    heapq.heappush(pq, (cost + 1, x, y - 1))
            if x < m - 1 and visited[x + 1][y] == False:
                if grid[x][y] == 3:
                    heapq.heappush(pq, (cost, x + 1, y))
                else:
                    heapq.heappush(pq, (cost + 1, x + 1, y))
            if y < n - 1 and visited[x][y + 1] == False:
                if grid[x][y] == 1:
                    heapq.heappush(pq, (cost, x, y + 1))
                else:
                    heapq.heappush(pq, (cost + 1, x, y + 1))
