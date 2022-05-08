import heapq


class Solution:
    def trapRainWater(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        pq = []

        for i in range(m):
            visited[i][0] = True
            heapq.heappush(pq, (grid[i][0], i, 0))
            visited[i][n - 1] = True
            heapq.heappush(pq, (grid[i][n - 1], i, n - 1))

        for j in range(n):
            visited[0][j] = True
            heapq.heappush(pq, (grid[0][j], 0, j))
            visited[m - 1][j] = True
            heapq.heappush(pq, (grid[m - 1][j], m - 1, j))

        res = 0
        while pq:
            val, x, y = heapq.heappop(pq)

            if x > 0 and visited[x - 1][y] == False:
                visited[x - 1][y] = True
                if grid[x - 1][y] < val:
                    res += (val - grid[x - 1][y])
                    grid[x - 1][y] = val
                heapq.heappush(pq, (grid[x - 1][y], x - 1, y))

            if y > 0 and visited[x][y - 1] == False:
                visited[x][y - 1] = True
                if grid[x][y - 1] < val:
                    res += (val - grid[x][y - 1])
                    grid[x][y - 1] = val
                heapq.heappush(pq, (grid[x][y - 1], x, y - 1))

            if x < m - 1 and visited[x + 1][y] == False:
                visited[x + 1][y] = True
                if grid[x + 1][y] < val:
                    res += (val - grid[x + 1][y])
                    grid[x + 1][y] = val
                heapq.heappush(pq, (grid[x + 1][y], x + 1, y))

            if y < n - 1 and visited[x][y + 1] == False:
                visited[x][y + 1] = True
                if grid[x][y + 1] < val:
                    res += (val - grid[x][y + 1])
                    grid[x][y + 1] = val
                heapq.heappush(pq, (grid[x][y + 1], x, y + 1))

        return res


class Solution:
    def trapRainWater(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        pq = []

        for i in range(m):
            visited.add((i, 0))
            heapq.heappush(pq, (grid[i][0], i, 0))
            visited.add((i, n - 1))
            heapq.heappush(pq, (grid[i][n - 1], i, n - 1))

        for j in range(n):
            visited.add((0, j))
            heapq.heappush(pq, (grid[0][j], 0, j))
            visited.add((m - 1, j))
            heapq.heappush(pq, (grid[m - 1][j], m - 1, j))

        res = 0
        while pq:
            val, x, y = heapq.heappop(pq)

            if x > 0 and (x - 1, y) not in visited:
                visited.add((x - 1, y))
                if grid[x - 1][y] < val:
                    res += (val - grid[x - 1][y])
                    grid[x - 1][y] = val
                heapq.heappush(pq, (grid[x - 1][y], x - 1, y))

            if y > 0 and (x, y - 1) not in visited:
                visited.add((x, y - 1))
                if grid[x][y - 1] < val:
                    res += (val - grid[x][y - 1])
                    grid[x][y - 1] = val
                heapq.heappush(pq, (grid[x][y - 1], x, y - 1))

            if x < m - 1 and (x + 1, y) not in visited:
                visited.add((x + 1, y))
                if grid[x + 1][y] < val:
                    res += (val - grid[x + 1][y])
                    grid[x + 1][y] = val
                heapq.heappush(pq, (grid[x + 1][y], x + 1, y))

            if y < n - 1 and (x, y + 1) not in visited:
                visited.add((x, y + 1))
                if grid[x][y + 1] < val:
                    res += (val - grid[x][y + 1])
                    grid[x][y + 1] = val
                heapq.heappush(pq, (grid[x][y + 1], x, y + 1))

        return res